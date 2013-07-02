from dvbobjects.PSI.NIT import *
import os
from dvbobjects.SBTVD.Descriptors import *

class NITObj:
    tvd_orig_network_id=0x073b
    tvd_ts_id=0x073b
    tvd_service_id_sd=0xe760
    ts_freq=533
    ts_remote_control_key=0x05
    
    def ObtenerNIT(self):
        nit = network_information_section(
                  network_id = self.tvd_orig_network_id,
                  network_descriptor_loop = [
                         network_descriptor(network_name = "LIFIATV",),
                         system_management_descriptor(
                              broadcasting_flag = 0,
                              broadcasting_identifier = 3,
                              additional_broadcasting_identification = 0x01,
                              additional_identification_bytes = [],
                              )
                         ],
                  transport_stream_loop = [
                       transport_stream_loop_item(
                              transport_stream_id = self.tvd_ts_id,
                              original_network_id = self.tvd_orig_network_id,
                              transport_descriptor_loop = [
                                   service_list_descriptor(
                                       dvb_service_descriptor_loop = [
                                              service_descriptor_loop_item (
                                                    service_ID = self.tvd_service_id_sd,
                                                    service_type = 1,
                                                    ),
                                              ],
                                       ),
                                   terrestrial_delivery_system_descriptor(
                                      area_code = 1341,
                                      guard_interval = 0x01,
                                      transmission_mode = 0x02,
                                      frequencies = [
                                                     tds_frequency_item( freq=self.ts_freq )
                                                     ],
                                      ),
                                   partial_reception_descriptor (
                                                                 service_ids = []
                                                                 ),
                                   transport_stream_information_descriptor (
                                        remote_control_key_id = self.ts_remote_control_key,
                                        ts_name = "LIFIATV",
                                        transmission_type_loop = [
                                              transmission_type_loop_item(
                                                      transmission_type_info = 0x0F,
                                                      service_id_loop = [
                                                             service_id_loop_item(
                                                                  service_id=self.tvd_service_id_sd
                                                                  ),
                                                             ]
                                                      ),
                                              transmission_type_loop_item(
                                                  transmission_type_info = 0xAF,
                                                  service_id_loop = [],
                                                  ),
                                              ],
                                        )
                                   ],
                          ),
                       ],
                  version_number = 0,
                  section_number = 0,
                  last_section_number = 0,
                  )
        return nit