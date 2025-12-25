/*
ZG0635	ZG05资管产品资产负债信息	"C1110_住户
C1210_住户"	业务逻辑类	数值比较校验	校验预警	产品资金募集信息期末产品份额住户与资产负债信息实收本金住户差异较大	"ZG04资管产品存续期募集信息 a
ZG05资管产品资产负债信息 b"	ABS(（a.期末产品份额，取地区代码="000000"的期末产品份额）-(b.C1110_住户+b.C1210_住户))/(b.C1110_住户+b.C1210_住户)>0.05	"a.客户类型=""1-住户"" and b.数据类型=""1-原币数据""
逐产品代码、币种比较"	"a.产品代码+a.币种=b.产品代码+b.币种
a.报送机构代码 =b.报送机构代码
a.数据日期=b.数据日期"	2021/9/1	2099/12/31	

ZG01    资管产品基本信息    ads_jgbs_rh_prd_baseinfo_sub
ZG02    资管产品初始募集信息  ads_jgbs_rh_prd_init_raising
ZG03    资管产品终止信息    ads_jgbs_rh_prd_baseinfo_end
ZG04    资管产品存续期募集信息 ads_jgbs_rh_prd_period_raising
ZG05    资管产品资产负债信息  ads_jgbs_rh_product_income_info
ZG06    资产收益权明细信息   手工
ZG07    除回购和拆借外贷款明细信息   ads_jgbs_rh_loan_detail_info
ZG08    特定目的载体交易对手明细信息  ads_jgbs_rh_spc_detail_info
ZG09    资产负债剩余期限信息  ads_jgbs_rh_adr_term_info
ZG10    债券等资产配置情况信息 ads_jgbs_rh_asset_config_info
ZG11    企业债券分行业、企业规模情况信息    ads_jgbs_rh_enterprise_bonds_scale_info
ZG12    除资产收益权外其他债权明细业务表    rh_other_creditor_rights_detail
rh_other_creditor_rights_detail

000000000

*/
select * from ads_jgbs_rh_asset_config_info where nj=20231231;
and data_type='1-原币数据';
