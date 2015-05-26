import psycopg2

connection = psycopg2.connect(database="cordex_esd_manager", host="localhost", user="postgres", password="Dumbo&2684")

submissions_cursor = connection.cursor()
uploads_cursor = connection.cursor()


# Get all submissions
submissions_cursor.execute("SELECT * FROM submissions_submission")
for submission in submissions_cursor:
	#print submission[0]

	# Get all uploads for this submission
	uploads_cursor.execute("SELECT * from submissions_upload WHERE submissions_upload.submission_id={};".format(submission[0]))

	for upload in uploads_cursor:
		print upload[7]

