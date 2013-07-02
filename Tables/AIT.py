from dvbobjects.MHP.AIT import *
from dvbobjects.MHP.Descriptors import *
from dvbobjects.SBTVD.Descriptors import *
import os

class AITObj:
    def ObtenerAIT(self):
        ait = application_information_section(
            application_type = 0x0009, # GINGA-NCL
            common_descriptor_loop = [],
            application_loop = [
               application_loop_item(
                  organisation_id = 0x0000000A,
                  application_id = 0x64,
                  application_control_code = 0x01, # AUTOSTART
                  
                  application_descriptors_loop = [
                      transport_protocol_descriptor(
                         protocol_id = 0x0001,
                         transport_protocol_label = 0,
                         remote_connection = 0,
                         component_tag = 0x0C, # association_tag
                      ),
                      application_descriptor(
                         application_profile = 0x0001,version_major = 1,
                         version_minor = 0,
                         version_micro = 0,
                         service_bound_flag = 1,
                         visibility = 3,
                         application_priority = 1,
                         transport_protocol_labels = [ 0 ],
                      ),
                                                      
                      application_name_descriptor(
                         application_name = "APP_GINGA"
                      ),
                                                      
                      ginga_ncl_application_descriptor(
                         parameters = [ ]
                      ),
                                                      
                      ginga_ncl_application_location_descriptor (
                        base_directory = "/",
                        class_path_extension = "",
                        initial_class = "cuadricula.ncl", # nombre del archivo NCL
                        # a ser ejecutado.
                      ),
                  ]
               ),                 
            ],
            version_number = 0,
            section_number = 0,
            last_section_number = 0,
        )
        return ait
    
    def CrearTS(self):
        ait=self.ObtenerAIT()
        out = open("./ait.sec", "wb")
        out.write(ait.pack())
        out.close()
        os.system("sec2ts " + str(2001) + " < ./ait.sec > ./ait.ts")
        print "AIT: Hecho"