create database spec2017

use spec2017;

drop table cpu2017;
create table cpu2017(
	benchmark varchar(32),
	hardware_vendor varchar(128),
	sys varchar(128),
	peak_result double(10, 2),
	base_result  

	
	energy_peak_result double(10, 2),
	energy_base_result double(10, 2),
	cores int,
	chips int, 
	enabled_threads_per_core tinyint(1),
	processor varchar(128),
	processor_mhz int,
	cpu_orderable varchar(64),
	parallel varchar(4),
	base_pointer_size varchar(32),
	peak_pointer_size varchar(32),
	first_level_cache varchar(128),
	second_level_cache varchar(128),
	third_level_cache varchar(128),
	other_cache varchar(128),
	memory varchar(128),
	storage text,
	operating_system varchar(256),
	file_system varchar(8),
	compiler varchar(512),
	hw_avail varchar(16),
	sw_avail varchar(16),
	license int,
	tested_by varchar(128),
	test_sponsor varchar(128),
	test_date varchar(16),
	published varchar(16),
	updated varchar(16),
	disclosure text,
	disclosures varchar(64));

drop table jbb2015;
create table jbb2015(
	benchmark varchar(32),
	company varchar(128),
	sys varchar(128),
	max_jops int,
	critical_jops int,
	jvm varchar(256),
	jvm_vendor varchar(64),
	of_nodes int,
	cores int,
	chips int,
	cores_per_chip int,
	of_threads_per_core int,
	total_of_threads int,
	processor varchar(128),
	cpu_speed int,
	cpu_characteristics varchar(256), 
	primary_cache varchar(64),
	secondary_cache varchar(128),
	tertiary_cache varchar(128),
	memory varchar(64) comment'大小: GB',
	dimms varchar(64),
	memory_details varchar(256),
	disk varchar(256),
	file_system varchar(32),
	operating_system varchar(128),
	os_vendor varchar(64),
	nics varchar(256),
	psu varchar(128),
	form_factor varchar(256),
	enclosure varchar(128),
	hw_avail varchar(16),
	os_avail varchar(16),
	jvm_avail varchar(16),
	sw_avail varchar(16),
	license int,
	tested_by varchar(128),
	test_sponsor varchar(128),
	test_date varchar(16),
	published varchar(16),
	updated varchar(16),
	disclosure text,
	disclosure_url varchar(64),
	disclosures varchar(64))

drop table power_ssj2008;
	
create table power_ssj2008(
	benchmark varchar(32),
	benchmark_version varchar(8),
	hardware_vendor varchar(128),
	sys varchar(128),
	nodes int,
	form_factor varchar(64),
	test_method varchar(32),
	res double,
	ssj_ops_100_of_target_load int,
	ssj_ops_90_of_target_load int,
	ssj_ops_80_of_target_load int,
	ssj_ops_70_of_target_load int,
	ssj_ops_60_of_target_load int,
	ssj_ops_50_of_target_load int,
	ssj_ops_40_of_target_load int,
	ssj_ops_30_of_target_load int,
	ssj_ops_20_of_target_load int,
	ssj_ops_10_of_target_load int,
	average_watts_100_of_target_load double,
	average_watts_90_of_target_load double,
	average_watts_80_of_target_load double,
	average_watts_70_of_target_load double,
	average_watts_60_of_target_load double,
	average_watts_50_of_target_load double,
	average_watts_40_of_target_load double,
	average_watts_30_of_target_load double,
	average_watts_20_of_target_load double,
	average_watts_10_of_target_load double,
	average_watts_active_idle double,
	performance_power_100_of_target_load double,
	performance_power_90_of_target_load double,
	performance_power_80_of_target_load double,
	performance_power_70_of_target_load double,
	performance_power_60_of_target_load double,
	performance_power_50_of_target_load double,
	performance_power_40_of_target_load double,
	performance_power_30_of_target_load double,
	performance_power_20_of_target_load double,
	performance_power_10_of_target_load double,
	cores int,
	chips int,
	cores_per_chip int,
	threads_per_core int,
	processor varchar(128),
	processor_mhz int,
	processor_characteristics varchar(128),
	cpu_orderable varchar(64),
	first_level_cache varchar(128),
	second_level_cache varchar(128),
	third_level_cache varchar(128),
	other_cache varchar(128),
	memory varchar(64) comment'大小: GB',
	operating_system varchar(256),
	operating_system_version varchar(256),
	file_system varchar(32),
	dimms varchar(64),
	memory_description varchar(512),
	network_controller tinyint unsigned,
	nics_connected tinyint unsigned,
	nics_enabled_firmware tinyint unsigned,
	nics_enabled_os tinyint unsigned,
	network_speed int,
	jvm_vendor varchar(64),
	jvm_version varchar(512),
	jvm_instances int,
	jvm_affinity text,
	jvm_bitness tinyint unsigned,
	jvm_options text,	
	initial_heap varchar(16),
	max_heap varchar(16),
	system_source varchar(64),
	system_designation varchar(128),
	power_provisioning varchar(128),
	disk_drive varchar(256),
	disk_controller varchar(256),
	power_management varchar(128),
	power_supply_details varchar(128),
	power_supplies_installed tinyint,
	power_supply_rating_watts int,
	hw_avail varchar(16),
	sw_avail varchar(16),
	license int,
	tested_by varchar(128),
	test_sponsor varchar(128),
	test_date varchar(16),
	published varchar(16),
	updated varchar(16),
	disclosure text,
	disclosure_url varchar(64),
	disclosures varchar(64))
	
drop table cpu2006;
create table cpu2006(
	benchmark varchar(32),
	hardware_vendor	varchar(128),
	sys varchar(128),
	res double,
	baseline double,
	cores int,
	chips int,
	cores_per_chip tinyint,
	threads_per_core tinyint,
	processor varchar(128),
	processor_mhz int,
	processor_characteristics text,
	cpu_orderable varchar(64),
	auto_parallelization varchar(8),
	base_pointer_size varchar(32),
	peak_pointer_size varchar(32),
	first_level_cache varchar(128),
	second_level_cache varchar(256),
	third_level_cache varchar(128),
	other_cache varchar(128),
	memory text,
	operating_system varchar(256),
	file_system varchar(128),
	compiler text,
	hw_avail varchar(16),
	sw_avail varchar(16),
	license int,
	tested_by varchar(16),
	test_sponsor varchar(64),
	test_date varchar(16),
	published varchar(16),
	updated varchar(16),
	disclosure text,
	disclosures varchar(64)
)

drop table jvm2008;
create table jvm2008(
	benchmark varchar(32),
	company varchar(32),
	sys varchar(64),
	res double,
	jvm varchar(128),
	cores tinyint,
	chips tinyint,
	cores_per_chip tinyint,
	logical_cpus_ int,
	processor varchar(128),
	cpu_speed double,
	first_cache varchar(128),
	second_cache varchar(128),
	other_cache varchar(128),
	memory text,
	os varchar(64),
	hw_avail varchar(16),
	os_avail varchar(16),
	sw_avail varchar(16),
	license int,
	tested_by varchar(32),
	test_date varchar(16),
	published varchar(16),
	updated varchar(16),
	disclosure varchar(256),
	disclosures varchar(64)
)

-- 建立机器学习特征表
create table ml_cpu2017_feature(
		benchmark varchar(32),
		sys varchar(128),
	    cores int,
        chips int,
        enabled_threads_per_core tinyint(1),
        processor_mhz int, 
        parallel tinyint(1),
        base_pointer_size tinyint(1) unsigned,
        peak_pointer_size tinyint(1) unsigned,
        first_level_cache int,
        second_level_cache int,
        third_level_cache int,
        other_cache int,
        memory int,
        storage int,
        base_result double,
        peak_result double
	)
	
create table cpu_api_info(
	benchmark varchar(32),
	sys varchar(128),
	cores int,
    chips int,
	enabled_threads_per_core int,
	processor_mhz int,	
    parallel varchar(4),
	base_pointer_size varchar(32),
	peak_pointer_size varchar(32),
    first_level_cache varchar(128),
	second_level_cache varchar(128),
	third_level_cache varchar(128),
	other_cache varchar(128),
	memory varchar(128),    
	storage text,
	update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)

drop table cpu_api_info 

replace into cpu_api_info (benchmark,sys,cores,chips
               ,enabled_threads_per_core,processor_mhz,parallel,base_pointer_size
               ,peak_pointer_size,first_level_cache,second_level_cache
               ,third_level_cache,other_cache,memory,storage)
               values ('CINT2017','myserver','8','1','2','3800','Yes','64-bit'
                       ,'64-bit','32 KB I + 32 KB D on chip per core','512 KB I+D on chip per core','32 MB I+D on chip per 8 cores','None','64 GB (2 x 32 GB 2Rx8 PC4-3200AA-E)  ','Micron 7400 PRO 960GB NVMe M.2')

select * from cpu_api_info 
	
select * from ml_cpu2017_feature

select distinct benchmark  from cpu2017 c  

select hardware_vendor, max(peak_result)
from cpu2017 c 
where benchmark = 'CINT2017'
group by hardware_vendor 


-- ==================================================================================================================================================================

--  仅考虑CPU2017 的统计量
	-- 不同芯片
		-- 不同芯片数量的处理器平均base result
		select chips, avg(base_result) as avg_base_result
		from cpu2017 c 
		where benchmark = 'CFP2017'
		group by chips
		order by chips
		
		-- 不同芯片数量的处理器平均base result
		select chips, avg(base_result) as avg_base_result
		from cpu2017 c 
		where benchmark = 'CINT2017'
		group by chips
		order by chips
	 
	-- 不同公司
		-- 不同公司所有送测的cpu的平均表现
		select hardware_vendor, avg(base_result) as avg_base_result
		from cpu2017 c 
		where benchmark = 'CINT2017'
		group by hardware_vendor 
		order by avg(base_result) desc
		limit 10
		
		-- 不同公司所有送测的system数量or占比
		(select hardware_vendor, sys_count / sys_tot_count as percentage
		from 
			(select hardware_vendor, count(distinct sys) as sys_count
			from cpu2017 c 
			group by hardware_vendor 
			order by count(distinct sys) desc) A
			cross join (select 
						count(distinct sys) as sys_tot_count
						from cpu2017) c2
		limit 5)
		UNION all
		(select '其他' as hardware_vendor, 1 - sum(percentage) as percentage
		from (select hardware_vendor, sys_count / sys_tot_count as percentage
				from 
					(select hardware_vendor, count(distinct sys) as sys_count
					from cpu2017 c 
					group by hardware_vendor 
					order by count(distinct sys) desc) A
					cross join (select 
								count(distinct sys) as sys_tot_count
								from cpu2017) c2
				limit 5) temp)
		
		-- 不同公司的吞吐量和时间相比
		select hardware_vendor
			, sum(case when benchmark = 'CFP2017' then base_result else 0 end) / sum(case when benchmark = 'CFP2017' then 1 else 0 end) as avg_speed_result 
			, sum(case when benchmark = 'CFP2017rate' then base_result else 0 end) / sum(case when benchmark = 'CFP2017rate' then 1 else 0 end) as avg_rate_result 
		from cpu2017 c 
		where benchmark like "CFP2017%"
		group by hardware_vendor
		order by avg_speed_result desc
		limit 5
			
		-- 不同公司的超过 某个值 的数量
		select hardware_vendor 
			, sum(case when base_result > 200 then 1 else 0 end) as exceed_cnts
		from cpu2017 c 
		where benchmark = 'CFP2017'
		group by hardware_vendor 
		order by exceed_cnts desc
		
		-- 不同公司的吞吐量和时间相比
			select hardware_vendor
				, sum(case when benchmark = 'CFP2017' then base_result else 0 end) / sum(case when benchmark = 'CFP2017' then 1 else 0 end) as avg_speed_result 
				, sum(case when benchmark = 'CFP2017rate' then base_result else 0 end) / sum(case when benchmark = 'CFP2017rate' then 1 else 0 end) as avg_rate_result 
			from cpu2017 c 
			where benchmark like "CFP2017%"
			group by hardware_vendor 
			order by avg_speed_result desc
			limit 5
		
			
		-- 不同公司的cint时间相比
			select hardware_vendor
				, AVG(base_result) avg_speed_result
			from cpu2017 c 
			where benchmark = "CINT2017"
			group by hardware_vendor 
			order by avg_speed_result desc
			limit 5
		
		-- 不同公司的cint吞吐量相比
			select hardware_vendor
				, AVG(base_result) avg_speed_result
			from cpu2017 c 
			where benchmark = "CINT2017rate"
			group by hardware_vendor 
			order by avg_speed_result desc
			limit 5
			
		-- 不同公司cfp吞吐量最大的硬件排行
			select hardware_vendor
				, max(base_result) max_rate_result
			from cpu2017 c 
			where benchmark = 'CFP2017rate'
			group by hardware_vendor 
			order by max_rate_result desc
			limit 5

	-- 不同时间角度
		-- 不同发布时期硬件cfp、cint的结果
		select year(hw_avail) as years
			, sum(case when benchmark = 'CFP2017' then base_result else 0 end) / sum(case when benchmark = 'CFP2017' then 1 else 0 end) as avg_speed_result
			, sum(case when benchmark = 'CFP2017rate' then base_result else 0 end) / sum(case when benchmark = 'CFP2017rate' then 1 else 0 end) as avg_rate_result
		from cpu2017 c 
		where year(hw_avail) >= '2016'
		group by years
		order by years 
		
		-- 最新的硬件产出日期
		select date_format(A.hw_avail, '%Y-%m') as recent_month, sys 
		from cpu2017 A 
			right join (select max(hw_avail) as hw_avail
						from cpu2017 c2) B
			on A.hw_avail = B.hw_avail
		order by sys desc
		limit 1
									
		-- cint2017最好的结果
		select base_result, sys
		from cpu2017 A 
			right join (select max(base_result) max_result
						from cpu2017
						where benchmark = 'CINT2017') B
					on A.base_result = B.max_result 
		where benchmark = 'CINT2017' 

		-- cintrate2017最好的结果
		select base_result, sys
		from cpu2017 A 
			right join (select max(base_result) max_result
						from cpu2017
						where benchmark = 'CINT2017rate') B
					on A.base_result = B.max_result 
		where benchmark = 'CINT2017rate' 
	
	select distinct benchmark from cpu2017 c 
			
-- jbb2015统计量
	-- 朴素统计量，最好效果的机器
	select max_jops, sys
	from jbb2015 A
		right join(
				select max(max_jops) as max_max_jops
				from jbb2015 j 
				where benchmark = 'JBB2015MULTI') B
			on A.max_jops = B.max_max_jops
	where benchmark = 'JBB2015MULTI'
	
	-- 不同时间下multi、comp、dist的平均表现
	select * 
	from 
		(select year(hw_avail) as years
			,sum(case when benchmark = 'JBB2015MULTI' then critical_jops else 0 end)
				/ sum(case when benchmark = 'JBB2015MULTI' then 1 else 0 end) as multi_res
			,sum(case when benchmark = 'JBB2015DIST' then critical_jops else 0 end)
				/ sum(case when benchmark = 'JBB2015DIST' then 1 else 0 end) as dist_res
			,sum(case when benchmark = 'JBB2015COMP' then critical_jops else 0 end)
				/ sum(case when benchmark = 'JBB2015COMP' then 1 else 0 end) as comp_res
		from jbb2015 j 
		group by years) A
	where A.years is not null and years > 2015
	order by years 
	
	-- 不同公司结果超过50000的服务器数量
		select company
			,sum(case when benchmark = 'JBB2015DIST' and critical_jops > 50000 then 1 else 0 end) as dist_cnt
			,sum(case when benchmark = 'JBB2015COMP' and critical_jops > 50000 then 1 else 0 end) as comp_cnt
			,sum(case when benchmark = 'JBB2015MULTI' and critical_jops > 50000 then 1 else 0 end) as multi_cnt
		from jbb2015 j 
		group by company 
		order by multi_cnt desc
		limit 10
	
	-- 不同核心数的表现（最大/critical）
		select of_threads_per_core
			,avg(critical_jops) as avg_critical_jops
			,max(max_jops) as max_max_jops
		from jbb2015 j 
		where benchmark = 'JBB2015MULTI'
		group by of_threads_per_core 
		order by of_threads_per_core 
	
-- power_ssj2008
	-- power2008不同服务器的能耗比
		select sys
			,avg(performance_power_100_of_target_load) as perform_100
		from power_ssj2008 ps 
		where benchmark_version = '1.2'
		group by sys
		order by perform_100 desc
		limit 10
		
	-- power2008不同核心performance
		select cores 
			, avg(performance_power_100_of_target_load) perfom_100
			, avg(performance_power_80_of_target_load) perfom_80
			, avg(performance_power_60_of_target_load) perfom_60
			, avg(performance_power_40_of_target_load) perfom_40
			, avg(performance_power_20_of_target_load) perfom_20
		from power_ssj2008 ps
		where benchmark_version = '1.2'
		group by cores 
		order by cores
	
	-- power2008不同节点数performance
		select nodes 
			,avg(performance_power_100_of_target_load) perfom_100
			,avg(performance_power_60_of_target_load) perfom_60
			,avg(performance_power_20_of_target_load) perfom_20
		from power_ssj2008 ps 
		where benchmark_version = '1.2'
		group by nodes
		order by nodes
		
	-- power2008不同benchmark_version占比
		select sum(case when benchmark_version = '0.23' then 1 else 0 end) / count(*) as percent_23
		 	,sum(case when benchmark_version = '1.1' then 1 else 0 end) / count(*) as percent_11
		 	,sum(case when benchmark_version = '1.2' then 1 else 0 end) / count(*) as percent_12
		from power_ssj2008 ps 
		
	-- power2008结果排行
		select sys
			,avg(res) as res 
		from power_ssj2008 ps 
		group by sys
		order by res desc
		limit 5
		
-- jvm2008
	-- jvm2008不同服务器的结果
		select sys
			,avg(res) as avg_res
		from jvm2008 j
		group by sys 
		order by avg_res desc
	
	-- jvm2008不同company结果percent
		select company
			,count(*) / avg(tot_cnt) as percent
		from jvm2008 A
			cross join (select count(*) as tot_cnt
						from jvm2008) B
		group by company 
		
	-- jvm2008不同核心数的result
		select cores
			,avg(res) res
		from jvm2008 j 
		group by cores
		order by cores
		
	-- jvm2008逻辑cpu分析
		select logical_cpus_ 
			, avg(res) as res
		from jvm2008 j 
		group by logical_cpus_ 
		order by logical_cpus_ 
		
	-- jvm2008硬件时期分析
		select DATE_FORMAT(hw_avail, '%Y-%m') as hw_month
			, avg(res) as res
		from jvm2008 j 
		where hw_avail is not null and hw_avail != ''
		group by hw_month 
		order by hw_month
		
				
		select * from ml_cpu2017_feature mcf 
-- 考虑 cpu2017 和 jbb2015的 统计量
	-- 需要注意的是，是否考虑将这两个表join起来产生新表？因为作join会很花时间
	-- 如果需要建新表，则需要把join的子查询换成新表名
	
	-- 不同服务器的 cpu平均base result 和 java应用程序的base result
		