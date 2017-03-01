import sys
from single_step import s

# s('rm myrepo')
s('git init')
    
# add a README file and commit
s('echo "This is my new repo" > README.txt')
s('git add .') 
s('git commit -m "first commit"')
    #https://github.com/ithenis/python-course.git
repo = "python-filescourse"
username = "ithenis"
password = raw_input("Enter password: ")        # diamond1
cmd = "git remote add origin https://{0}:{1}@github.com/{0}/{2}.git".format(username, password, repo)


# make sure you have created the remote repo: myrepo
s(cmd)
s('git remote -v')
s('git push -u origin master')