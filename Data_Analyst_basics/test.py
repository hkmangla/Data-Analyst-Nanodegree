import unicodecsv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np

with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

with open('daily_engagement.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)

with open('project_submissions.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)

def parse_date(date):
    if date == '':
        return None
    else:
    	return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
    if i == '':
    	return None
    else:
    	return int(i)

   	
for enrollment in enrollments:
	enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
	enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
	enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
	enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
	enrollment['join_date'] = parse_date(enrollment['join_date'])


for engagement_record in daily_engagement:
	engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
	engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
	engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
	engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
	engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

for submission in project_submissions:
	submission['completion_date'] = parse_date(submission['completion_date'])
	submission['creation_date'] = parse_date(submission['creation_date'])


def check_id(enrollments):
	unique_id = []
	enrollment_num_unique_students = 0
	for i in enrollments:
		if i['account_key'] not in unique_id:
			unique_id.append(i['account_key'])
			enrollment_num_unique_students += 1
	return unique_id		

enrollment_num_rows = len(enrollments)
engagement_num_rows = len(daily_engagement)
submission_num_rows = len(project_submissions)

enrollment_num_unique_students = len(check_id(enrollments))
engagement_num_unique_students = 0
unique_id = []
for i in daily_engagement:
	if i['acct'] not in unique_id:
		unique_id.append(i['acct'])
		engagement_num_unique_students += 1
	i['account_key'] = i['acct']
	del i['acct']		

submission_num_unique_students = len(check_id(project_submissions))
v = 0
y = unique_id
x = check_id(enrollments)
for item in enrollments:
    iyt = item['account_key']
    if iyt not in y and item['join_date'] != item['cancel_date']:
		v += 1


udacity_test_account = set()
for enrollment in enrollments:
	if enrollment['is_udacity']:
		udacity_test_account.add(enrollment['account_key'])


def remove_udacity_account(data):
	non_udacity = []
	for datalist in data:
		if datalist['account_key'] not in udacity_test_account:
			non_udacity.append(datalist)
	return non_udacity					

non_udacity_enrollments = remove_udacity_account(enrollments)
non_udacity_engagements = remove_udacity_account(daily_engagement)
non_udacity_submissions = remove_udacity_account(project_submissions)

paid_students = {}

for enrollment in non_udacity_enrollments:
	if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
		if enrollment['account_key'] not in paid_students or enrollment['join_date'] > paid_students[enrollment['account_key']]:
			paid_students[enrollment['account_key']] = enrollment['join_date'] 

def within_one_week(join_date, engagement_date):
	time_delta = engagement_date - join_date
	return time_delta.days < 7 and time_delta.days >=0

paid_engagement_in_first_week = []

for data in daily_engagement:
	if data['account_key'] in paid_students.keys():
		if within_one_week(paid_students[data['account_key']],data['utc_date']):
			paid_engagement_in_first_week.append(data)

def group_by_account(data,key):
	enagaged_by_account = defaultdict(list)
	for engaged in data:
		account_key = engaged[key]
		enagaged_by_account[account_key].append(engaged)
	return enagaged_by_account

enagaged_by_account = group_by_account(paid_engagement_in_first_week,'account_key')
def total_num_of_by_account(enagaged_by_account,key):
	total_minutes_by_account = {}
	for account_key,engaged_record in enagaged_by_account.items():
		total_minutes = 0
		for i in engaged_record:
			total_minutes += i[key]
		total_minutes_by_account[account_key] = total_minutes	
	return total_minutes_by_account


total_minutes_by_account = total_num_of_by_account(enagaged_by_account,'total_minutes_visited')
tatal_lesson_completed_by_account = total_num_of_by_account(enagaged_by_account,'lessons_completed')
# total_num_of_day_visited = total_num_of_by_account(enagaged_by_account,'has_visited')

subway_project_lesson_keys = ['746169184', '3176718735']

passing_engagement = []
non_passing_engagement = []

passing_project_keys = set()
for submission in non_udacity_submissions:
	if submission['lesson_key'] in subway_project_lesson_keys:
		if submission['assigned_rating'] == 'PASSED' or submission['assigned_rating'] == 'DISTINCTION':
			passing_project_keys.add(submission['account_key'])
# print len(passing_project_keys)			

for engaged in paid_engagement_in_first_week:
	if engaged['account_key'] in passing_project_keys:
		passing_engagement.append(engaged)
	else:
		non_passing_engagement.append(engaged)

# print len(passing_engagement)
# print len(non_passing_engagement)


passing_engagement_by_account = group_by_account(passing_engagement,'account_key')
non_passing_engagement_by_account = group_by_account(non_passing_engagement,'account_key')

total_minutes_in_passing_engagement = total_num_of_by_account(passing_engagement_by_account,'total_minutes_visited')
total_minutes_in_non_passing_engagement = total_num_of_by_account(non_passing_engagement_by_account,'total_minutes_visited')

# total_minutes = total_minutes_in_passing_engagement.values()
# print np.mean(total_minutes)

# total_minutes = total_minutes_in_non_passing_engagement.values()
# print np.mean(total_minutes)



# total_minutes = total_minutes_by_account.values()
# max_minutes = np.max(total_minutes)
# for account_key,engaged_record in enagaged_by_account.items():
# 	if total_minutes_by_account[account_key] == max_minutes:
# 		print engaged_record

# print len(paid_engagement_in_first_week)
# print daily_engagement[0]['account_key']
# print enrollment_num_rows
# print engagement_num_rows
# print submission_num_rows
# print enrollment_num_unique_students
# print engagement_num_unique_students
# print submission_num_unique_students



# print enrollments[0]
# print daily_engagement[0]
# print project_submissions[0]    