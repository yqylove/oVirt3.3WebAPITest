#coding:utf-8

__authors__ = ['"Liu Fei" <fei.liu@cs2c.com.cn>']
__version__ = "V0.1"

'''
# ChangeLog:
#---------------------------------------------------------------------------------
# Version        Date                Desc                            Author
#---------------------------------------------------------------------------------
# V0.1           2014/11/04          初始版本                                                            Liu Fei 
#---------------------------------------------------------------------------------
'''

from TestData.VirtualMachine import ITC05_SetUp as ModuleData

'''
---------------------------------------------------------------------------------------------------
@note: Pre-Test-Data
---------------------------------------------------------------------------------------------------
'''
vm_name = "vm-ITC05020403"

xml_vm_info='''
<vm>
    <name>%s</name>
    <type>server</type>
    <memory>536870912</memory>
    <cluster>
        <name>%s</name>
    </cluster>
    <template>
        <name>Blank</name>
    </template>
    <cpu>
        <topology sockets="1" cores="1"/>
    </cpu>
    <os>
        <boot dev="cdrom"/>
        <boot dev="hd"/>
    </os>
</vm>
''' % (vm_name, ModuleData.cluster_nfs_name)



'''
---------------------------------------------------------------------------------------------------
@note: Test-Data
---------------------------------------------------------------------------------------------------
'''



'''
---------------------------------------------------------------------------------------------------
@note: Post-Test-Data
---------------------------------------------------------------------------------------------------
'''




'''
---------------------------------------------------------------------------------------------------
@note: ExpectedResult
---------------------------------------------------------------------------------------------------
'''
expected_status_code_suspend_vm_suspended = 409
expected_info_suspend_vm_suspended = '''
<action>
    <status>
        <state>failed</state>
    </status>
    <fault>
        <reason>Operation Failed</reason>
        <detail>[Cannot hibernate VM. VM is not up.]</detail>
    </fault>
</action>
'''


