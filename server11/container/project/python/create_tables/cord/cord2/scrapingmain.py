from from_dospara import get_parts

from insert_ssd import ssdmain
from insert_motherboard import mothermain
from insert_cpu import cpumain
from insert_memory import memorymain
from insert_hdd import hddmain
from insert_power import powermain
from insert_case import casemain
from insert_casecooler import casecoolermain
from insert_cpucooler import cpucoolermain

def scraping():
    item_list = get_parts()  # 引数を省略しても全種取得可

    cpu = cpumain
    mother = mothermain
    ssd = ssdmain
    memory = memorymain
    hdd = hddmain
    case = casemain
    power = powermain
    casecooler = casecoolermain
    cpucooler = cpucoolermain

    cpu_list = item_list['amdCPU'] + item_list['intelCPU']
    if cpu_list != None:
        cpu.insertcpu(cpu_list)
    if item_list['motherBoard'] != None:
        mother.insertmother(item_list['motherBoard'])
    if item_list['SSD'] != None:
        ssd.insertssd(item_list['SSD'])
    if item_list['memory'] != None :
        memory.insertmemory(item_list['memory'])
    if item_list['HDD'] != None:
        hdd.inserthdd(item_list['HDD'])
    if item_list['case'] != None:
        case.insertcase(item_list['case'])
    if item_list['power'] != None:
        power.insertpower(item_list['power'])
    cpucooler_list = item_list['cpuAirCooler'] + item_list['cpuLiquidCooler']
    if cpucooler_list != None:
        cpucooler.insertcpucooler(cpucooler_list)
    if item_list['caseCooler'] != None:
        casecooler.insertcasecooler(item_list['caseCooler'])
    
