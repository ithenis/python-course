from single_step import s
#git@github.com:ithenis/python-course.git
repo = "python-course"
username = "ithenis"
password = raw_input("Enter password: ")        # diamond1
cmd = "git remote add origin https://{0}:{1}@github.com/{0}/{2}.git".format(username, password, repo)



s('cd myrepo')
# make sure you have created the remote repo: myrepo
s(cmd)
s('git remote -v')
s('git push -u origin master')

