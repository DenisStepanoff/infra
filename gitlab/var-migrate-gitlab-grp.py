#export/import gitlab ci variables between two gitlab servers between two groups

import gitlab #pip3 install --upgrade python-gitlab
import os
import ast

#projectsIDs format: [[sourceProject-1-ID, destinationProject-1-ID], [sourceProject-2-ID, destinationProject-2-ID], ...]
projectsIDs = [[123456, 34567],]

SOURCE_GL_TOKEN =os.environ['MY_PERS_TOKEN']    #personal gitlab token from os env. variable (export MY_PERS_TOKEN=ExAmplEGitLAbtoKen)
SOURCE_GITLAB_ENDPOINT = "https://gitlabsrc.my.local" #gitlab server ip or fqdn

DEST_GL_TOKEN =os.environ['MY_PERS_TOKEN2']
DEST_GITLAB_ENDPOINT = "https://gitlabdest.my.local"

glSource = gitlab.Gitlab(url=SOURCE_GITLAB_ENDPOINT, private_token=SOURCE_GL_TOKEN)
glDest = gitlab.Gitlab(url=DEST_GITLAB_ENDPOINT, private_token=DEST_GL_TOKEN)

for ids in projectsIDs:
    sourceGroup = glSource.groups.get(ids[0])
    destGroup = glDest.groups.get(ids[1])
    print("Source Group: " + sourceGroup.name)
    print("Destination Group: " + destGroup.name)
    gVariables = sourceGroup.variables.list()
    print(gVariables)

    for var in gVariables:
        print("Create var: " + var.key)
        destGroup.variables.create(ast.literal_eval(str(var)[str(var).find("{"):]))
