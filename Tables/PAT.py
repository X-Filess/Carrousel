from dvbobjects.PSI.PAT import *
import os


class PATObj:
    tvd_ts_id = 0x073b
    tvd_service_id_sd = 0x073b
    tvd_pmt_pid_sd = 1031
    def ObtenerPAT(self):
        pat = program_association_section(
                                          transport_stream_id = self.tvd_ts_id,
                                          program_loop = [
                                                          program_loop_item(
                                                                            # Programa especial para la tabla NIT
                                                                            program_number = 0,
                                                                            PID = 16,
                                                                            ),
                                                          program_loop_item(
                                                                            program_number = self.tvd_service_id_sd,
                                                                            PID = self.tvd_pmt_pid_sd,
                                                                            ),
                                                          ],
                                          version_number = 0,
                                          section_number = 0,
                                          last_section_number = 0,
                                          )
        return pat
    
    def CrearTS(self):
        pat = self.ObtenerPAT()
        out = open("./pat.sec", "wb")
        out.write(pat.pack())
        out.close()
        os.system("sec2ts 0 < ./pat.sec > ./pat.ts")
        print "PAT: Hecho"
        