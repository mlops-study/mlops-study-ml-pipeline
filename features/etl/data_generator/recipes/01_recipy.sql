/** 20230618 --> {{ params.base_day }} */

/** 1. Recipy 테이블 데이터 생성
  */
create database if not exists recipy;

drop table if exists recipy.recipy_target_applicants;
create table recipy.recipy_target_applicants as
select a.applicant_id
      ,a.loan_account_id
  from mlops.loan_applicant_info a
 where a.applicant_date between '20230601' and '20231130'
   and rand({{ params.base_day }}) < 0.10
;

drop table if exists recipy.recipy_target_applicants_new_id;
create table recipy.recipy_target_applicants_new_id as
select a.applicant_id
      ,concat(substr('{{ params.base_day }}', 3), lpad(cast(a.idx as char(4)), 4, '0')) as new_applicant_id
      ,a.loan_account_id
      ,concat('LA', substr('{{ params.base_day }}', 3), lpad(cast(a.idx as char(4)), 4, '0')) as new_loan_account_id
  from (select a.applicant_id
              ,a.loan_account_id
              ,row_number() over (order by a.applicant_id desc) as idx
          from recipy.recipy_target_applicants a
       ) a
;

--/** 2. Recipy 테이블 데이터 생성
--  */
--
--/** mlops.cust_info */
--delete
--  from mlops.cust_info a
-- where a.base_dt = '{{ params.base_day }}'
--;
--
--insert
--  into mlops.cust_info
--      (base_dt
--      ,cust_id
--      ,gender
--      ,married
--      ,education
--      ,self_employed)
--select '{{ params.base_day }}' as base_dt
--      ,a.cust_id
--      ,a.gender
--      ,a.married
--      ,a.education
--      ,a.self_employed
--  from mlops.cust_info a
-- where a.base_dt = '20231130'
--;
--
--/** mlops.family_info */
--delete
--  from mlops.family_info a
-- where a.base_dt = '{{ params.base_day }}'
--;
--
--insert
--  into mlops.family_info
--      (base_dt
--      ,cust_id
--      ,family_cust_id
--      ,living_together
--      )
--select '{{ params.base_day }}' as base_dt
--      ,a.cust_id
--      ,a.family_cust_id
--      ,a.living_together
--  from mlops.family_info a
-- where a.base_dt = '20231130'
--;
--
--
--/** mlops.loan_applicant_info */
--delete a
--  from mlops.loan_applicant_info a
-- where a.applicant_id in (select b.new_applicant_id
--                            from recipy.recipy_target_applicants_new_id b
--                         )
--;
--
--insert
--  into mlops.loan_applicant_info
--      (applicant_id
--      ,applicant_date
--      ,applicant_time
--      ,cust_id
--      ,applicant_income
--      ,coapplicant_income
--      ,credit_history
--      ,property_area
--      ,loan_amount
--      ,loan_amount_term
--      ,loan_account_id
--      )
--select a.new_applicant_id as applicant_id
--      ,'{{ params.base_day }}' as applicant_date
--      ,b.applicant_time
--      ,b.cust_id
--      ,b.applicant_income
--      ,b.coapplicant_income
--      ,b.credit_history
--      ,b.property_area
--      ,b.loan_amount
--      ,b.loan_amount_term
--      ,a.new_loan_account_id as loan_account_id
--  from recipy.recipy_target_applicants_new_id a inner join
--       mlops.loan_applicant_info b on (a.applicant_id = b.applicant_id)
--;
--
--
--/** mlops.loan_default_account */
--delete a
--  from mlops.loan_default_account a
-- where a.loan_account_id in (select b.new_loan_account_id
--                               from recipy.recipy_target_applicants_new_id b
--                            )
--;
--
--insert
--  into mlops.loan_default_account
--      (loan_account_id
--      ,registration_date
--      ,registration_time
--      ,loan_default
--      )
--select c.loan_account_id
--      ,date_format(date_add(str_to_date('{{ params.base_day }}', '%Y%m%d'), INTERVAL c.plus_days DAY), '%Y%m%d') as registration_date
--      ,c.registration_time
--      ,c.loan_default
--  from (select a.new_loan_account_id as loan_account_id
--              ,abs(datediff(str_to_date('{{ params.base_day }}', '%Y%m%d'), str_to_date(b.registration_date, '%Y%m%d'))) % 89
--                  as plus_days
--              ,b.registration_time
--              ,b.loan_default
--          from recipy.recipy_target_applicants_new_id a inner join
--               mlops.loan_default_account b on (a.loan_account_id = b.loan_account_id)
--       ) c
--;
