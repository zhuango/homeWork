select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-18 00:00:00' group by  user_id into outfile'/var/lib/mysql-files/buser_click.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-18 00:00:00' group by  user_id into outfile'/var/lib/mysql-files/buser_collect.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-18 00:00:00' group by  user_id into outfile'/var/lib/mysql-files/buser_cart.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-18 00:00:00' group by  user_id into outfile'/var/lib/mysql-files/buser_buy.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-18 00:00:00' group by  item_id into outfile'/var/lib/mysql-files/bitem_click.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-18 00:00:00' group by  item_id into outfile'/var/lib/mysql-files/bitem_collect.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-18 00:00:00' group by  item_id into outfile'/var/lib/mysql-files/bitem_cart.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-18 00:00:00' group by  item_id into outfile'/var/lib/mysql-files/bitem_buy.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-18 00:00:00' group by  user_id,item_id into outfile'/var/lib/mysql-files/bu_it_click.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-18 00:00:00' group by  user_id,item_id into outfile'/var/lib/mysql-files/bu_it_collect.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-18 00:00:00' group by  user_id,item_id into outfile'/var/lib/mysql-files/bu_it_cart.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-18 00:00:00' group by  user_id,item_id into outfile'/var/lib/mysql-files/bu_it_buy.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 group by user_id into outfile '/var/lib/mysql-files/nuser_click.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 group by user_id into outfile '/var/lib/mysql-files/nuser_collect.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 group by user_id into outfile '/var/lib/mysql-files/nuser_cart.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 group by user_id into outfile '/var/lib/mysql-files/nuser_buy.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 group by item_id into outfile '/var/lib/mysql-files/nitem_click.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 group by item_id into outfile '/var/lib/mysql-files/nitem_collect.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 group by item_id into outfile '/var/lib/mysql-files/nitem_cart.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 group by item_id into outfile '/var/lib/mysql-files/nitem_buy.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 group by  user_id,item_id into outfile '/var/lib/mysql-files/nu_it_click.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 group by  user_id,item_id into outfile '/var/lib/mysql-files/nu_it_collect.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 group by  user_id,item_id into outfile '/var/lib/mysql-files/nu_it_cart.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 group by  user_id,item_id into outfile '/var/lib/mysql-files/nu_it_buy.txt';
 
 
 
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id into outfile '/var/lib/mysql-files/buser_recent3day_click.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id into outfile '/var/lib/mysql-files/buser_recent3day_collect.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id into outfile '/var/lib/mysql-files/buser_recent3day_cart.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id into outfile '/var/lib/mysql-files/buser_recent3day_buy.txt';
 
 
 
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by item_id into outfile '/var/lib/mysql-files/bitem_recent3day_click.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by item_id into outfile '/var/lib/mysql-files/bitem_recent3day_collect.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by item_id into outfile '/var/lib/mysql-files/bitem_recent3day_cart.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by item_id into outfile '/var/lib/mysql-files/bitem_recent3day_buy.txt';

select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/bu_it_recent3day_click.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/bu_it_recent3day_collect.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/bu_it_recent3day_cart.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-18 00:00:00' and time>'2014-12-15 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/bu_it_recent3day_buy.txt';
 
 
 
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id into outfile '/var/lib/mysql-files/nuser_recent3day_click.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id into outfile '/var/lib/mysql-files/nuser_recent3day_collect.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id into outfile '/var/lib/mysql-files/nuser_recent3day_cart.txt';
select user_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id into outfile '/var/lib/mysql-files/nuser_recent3day_buy.txt';
 
 
 
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by item_id into outfile '/var/lib/mysql-files/nitem_recent3day_click.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by item_id into outfile '/var/lib/mysql-files/nitem_recent3day_collect.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by item_id into outfile '/var/lib/mysql-files/nitem_recent3day_cart.txt';
select item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by item_id into outfile '/var/lib/mysql-files/nitem_recent3day_buy.txt';
 
 
 
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=1 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/nu_it_recent3day_click.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=2 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/nu_it_recent3day_collect.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=3 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/nu_it_recent3day_cart.txt';
select user_id,item_id,count(behavior_type) from dutir_tianchi_mobile_recommend_train_user_train where behavior_type=4 andtime<'2014-12-19 00:00:00' and time>'2014-12-16 00:00:00' group by user_id,item_id into outfile'/var/lib/mysql-files/nu_it_recent3day_buy.txt';