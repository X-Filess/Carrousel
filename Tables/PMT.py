from dvbobjects.PSI.PMT import *
from dvbobjects.SBTVD.Descriptors import *
from dvbobjects.MHP.Descriptors import *
import os

class PMTObj:
    tvd_pmt_pid_sd= 1031 # PID de la PMT del servicio.
    def ObtenerPMT(self):
        pmt_sd = program_map_section(
            program_number = 5555, #tvd_service_id_sd,
            PCR_PID = 2064,
            program_info_descriptor_loop = [],
            stream_loop = [
                           stream_loop_item(
                                            stream_type = 27, # mpeg2 video stream type
                                            elementary_PID = 4113,
                                            element_info_descriptor_loop = [
                                                                            ]
                                            ),
                           stream_loop_item(
                                            stream_type = 15, # mpeg2 audio stream type
                                            elementary_PID = 4352,
                                            element_info_descriptor_loop = []
                                            ),
                           stream_loop_item(
                                            stream_type = 5, # AIT stream type
                                            elementary_PID = 2001,
                                            element_info_descriptor_loop = [
                                                                            data_component_descriptor (
                                                                                                       data_component_id = 0xA3, # sistema AIT
                                                                                                       additional_data_component_info = ait_identifier_info(
                                                                                                                                                            application_type = GINGA_NCL_application_type,
                                                                                                                                                            ait_version = 0                                                                                                                                          
                                                                                                                                                            ).bytes(),
                                                                                                       ),
                                                                            application_signalling_descriptor(
                                                                                                              application_type = 9, # 9 GINGA-NCL
                                                                                                              AIT_version = 1, # current ait version
                                                                                                 ),
                                                                            ]
                                            ),
                           stream_loop_item(
                                            stream_type = 0x0B, # DSMCC stream type
                                            elementary_PID = 2004,
                                            element_info_descriptor_loop = [
                                                                            association_tag_descriptor(
                                                                                                       association_tag = 0x0C,
                                                                                                       use = 0,
                                                                                                       selector_lenght = 0,
                                                                                                       transaction_id = 0x80000000,timeout = 0xFFFFFFFF,
                                                                                                       private_data = "",
                                                                                                       ),
                                                                            stream_identifier_descriptor(
                                                                                                         component_tag = 0x0C,
                                                                                                         ),
                                                                            carousel_identifier_descriptor(
                                                                                                           carousel_ID = 2,
                                                                                                           format_ID = 0,
                                                                                                           private_data = "",
                                                                                                           ),
                                                                            data_component_descriptor (
                                                                                                       data_component_id = 0xA0, # sistema GINGA
                                                                                                       additional_data_component_info = additional_ginga_j_info(
                                                                                                                                                                transmission_format = 0x2,
                                                                                                                                                                document_resolution = 0x5,
                                                                                                                                                                organization_id
                                                                                                                                                                = 0x0000000A,
                                                                                                                                                                application_id
                                                                                                                                                                = 0x0064,
                                                                                                                                                                carousel_id
                                                                                                                                                                = 2,
                                                                                                                                                                ).bytes(),
                                                                                                       ),
                                                                            ]
                                            )
                           ],
            version_number = 0,
            section_number = 0,
            last_section_number = 0,
            )
        return pmt_sd
    
    def CrearTS(self):
        pmt_sd = self.ObtenerPMT()
        out = open("./pmt_sd.sec", "wb")
        out.write(pmt_sd.pack())
        out.close()
        os.system("sec2ts " + str(self.tvd_pmt_pid_sd) + " < ./pmt_sd.sec > ./pmt_sd.ts")
        print "PMT: Hecho"
        