import PMT
import AIT
import PAT
import os

AITTable = AIT.AITObj()
AITTable.CrearTS()

PMTTable = PMT.PMTObj()
PMTTable.CrearTS()

PATTable = PAT.PATObj()
PATTable.CrearTS()

os.system("tscbrmuxer 600000 b:15040 pat.ts b:15040 pmt_sd.ts b:3008 ait.ts b:400000 app_ginga.ts b:245800 Audio.ts b:1590000 Video.ts > ./MUX/prueba.ts")
os.system("tsstamp ./MUX/prueba.ts 2268888 > ./MUX/prueba1.fixed.ts")


