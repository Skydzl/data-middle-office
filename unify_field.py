#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:44:25 2023

@author: zby
"""


def get_db_field_name(tablename):
    if tablename == 'cpu2017':
        db_field_name = ['benchmark','hardware_vendor','sys'
                         ,'peak_result','base_result','energy_peak_result'
                         ,'energy_base_result','cores','chips'
                         ,'enabled_threads_per_core','processor','processor_mhz'
                         ,'cpu_orderable','parallel','base_pointer_size'
                         ,'peak_pointer_size','first_level_cache','second_level_cache'
                         ,'third_level_cache','other_cache','memory'
                         ,'storage','operating_system','file_system'
                         ,'compiler','hw_avail','sw_avail'
                         ,'license','tested_by','test_sponsor'
                         ,'test_date','published','updated'
                         ,'disclosure','disclosures']
        
    elif tablename == 'jbb2015':
        db_field_name = ['benchmark','company','sys'
                         ,'max_jops','critical_jops','jvm'
                         ,'jvm_vendor','of_nodes','cores'
                         ,'chips','cores_per_chip','of_threads_per_core'
                         ,'total_of_threads','processor','cpu_speed'
                         ,'cpu_characteristics','primary_cache','secondary_cache'
                         ,'tertiary_cache','memory','dimms'
                         ,'memory_details','disk','file_system'
                         ,'operating_system','os_vendor','nics'
                         ,'psu','form_factor','enclosure'
                         ,'hw_avail','os_avail','jvm_avail'
                         ,'sw_avail','license','tested_by'
                         ,'test_sponsor','test_date','published'
                         ,'updated','disclosure','disclosure_url'
                         ,'disclosures']
        
    elif tablename == 'power_ssj2008':
        db_field_name = ['benchmark','benchmark_version','hardware_vendor'
                         ,'sys','nodes','form_factor'
                         ,'test_method','res','ssj_ops_100_of_target_load'
                         ,'ssj_ops_90_of_target_load','ssj_ops_80_of_target_load','ssj_ops_70_of_target_load'
                         ,'ssj_ops_60_of_target_load','ssj_ops_50_of_target_load','ssj_ops_40_of_target_load'
                         ,'ssj_ops_30_of_target_load','ssj_ops_20_of_target_load','ssj_ops_10_of_target_load'
                         ,'average_watts_100_of_target_load','average_watts_90_of_target_load','average_watts_80_of_target_load'
                         ,'average_watts_70_of_target_load','average_watts_60_of_target_load','average_watts_50_of_target_load'
                         ,'average_watts_40_of_target_load','average_watts_30_of_target_load','average_watts_20_of_target_load'
                         ,'average_watts_10_of_target_load','average_watts_active_idle','performance_power_100_of_target_load'
                         ,'performance_power_90_of_target_load','performance_power_80_of_target_load','performance_power_70_of_target_load'
                         ,'performance_power_60_of_target_load','performance_power_50_of_target_load','performance_power_40_of_target_load'
                         ,'performance_power_30_of_target_load','performance_power_20_of_target_load','performance_power_10_of_target_load'
                         ,'cores','chips','cores_per_chip'
                         ,'threads_per_core','processor','processor_mhz'
                         ,'processor_characteristics','cpu_orderable','first_level_cache'
                         ,'second_level_cache','third_level_cache','other_cache'
                         ,'memory','operating_system','operating_system_version'
                         ,'file_system','dimms','memory_description'
                         ,'network_controller','nics_connected','nics_enabled_firmware'
                         ,'nics_enabled_os','network_speed','jvm_vendor'
                         ,'jvm_version','jvm_instances','jvm_affinity'
                         ,'jvm_bitness','jvm_options','initial_heap'
                         ,'max_heap','system_source','system_designation'
                         ,'power_provisioning','disk_drive','disk_controller'
                         ,'power_management','power_supply_details','power_supplies_installed'
                         ,'power_supply_rating_watts','hw_avail','sw_avail'
                         ,'license','tested_by','test_sponsor'
                         ,'test_date','published','updated'
                         ,'disclosure','disclosure_url','disclosures']
        
    elif tablename == 'cpu2006':
        db_field_name = ['benchmark','hardware_vendor','sys'
                        ,'res','baseline','cores'
                        ,'chips','cores_per_chip','threads_per_core'
                        ,'processor','processor_mhz','processor_characteristics'
                        ,'cpu_orderable','auto_parallelization','base_pointer_size'
                        ,'peak_pointer_size','first_level_cache','second_level_cache'
                        ,'third_level_cache','other_cache','memory'
                        ,'operating_system','file_system','compiler'
                        ,'hw_avail','sw_avail','license'
                        ,'tested_by','test_sponsor','test_date'
                        ,'published','updated','disclosure'
                        ,'disclosures']
    
    elif tablename == 'jvm2008':
        db_field_name = ['benchmark','company','sys'
                        ,'res','jvm','cores'
                        ,'chips','cores_per_chip','logical_cpus_'
                        ,'processor','cpu_speed','first_cache'
                        ,'second_cache','other_cache','memory'
                        ,'os','hw_avail','os_avail'
                        ,'sw_avail','license','tested_by'
                        ,'test_date','published','updated'
                        ,'disclosure','disclosures']
    return db_field_name


def unify_field_name(raw_data, tablename):
    """
    :param raw_data: DataFrame obj 待处理数据
    :return: 将所有的列名中的符号和空格去掉
    """
    raw_columns = raw_data.columns
    db_field_name = get_db_field_name(tablename)
    rename_dict = dict(zip(raw_columns, db_field_name))
    return raw_data.rename(rename_dict, axis=1)
