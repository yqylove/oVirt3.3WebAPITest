#encoding:utf-8


from Configs import GlobalConfig
import ITC03_SetUp as DM

'''
@note: Pre-TestData
'''
# 配置电源管理选项的host的相关信息
host = GlobalConfig.Hosts['node1']
host_name = 'node-ITC03011001'
xml_host_info = '''
<host>
    <name>%s</name>
    <address>%s</address>
    <root_password>%s</root_password>
    <cluster>
        <name>%s</name>
    </cluster>
</host>
''' % (host_name, host['ip'], \
       host['password'], \
       DM.cluster_name)

'''
@note: Test-Data
'''
iscsi_server_ip = GlobalConfig.DataStorages['iscsi']['data1-iscsi']['ip']
iscsi_server_port = GlobalConfig.DataStorages['iscsi']['data1-iscsi']['port']
xml_iscsi_info = '''
<action>
    <iscsi>
        <address>%s</address>
        <port>%s</port>
    </iscsi>
</action>
''' % (iscsi_server_ip, iscsi_server_port)

'''
@note: Post-TestData
'''
# 资源清理时删除host所用的选项（强制删除/同步）
xml_host_del_option = '''
<action>
    <force>true</force>
    <async>false</async>
</action>
'''

'''
@note: ExpectedResult
'''
expected_status_code_create_host = 201          # 创建主机操作的期望状态码
expected_status_code_discovery_iscsi = 200      # 成功探测到iscsi服务器时，返回状态码
expected_status_code_deactive_host = 200        # 维护主机操作的期望状态码
expected_status_code_del_host = 200             # 删除主机操作的期望状态码
