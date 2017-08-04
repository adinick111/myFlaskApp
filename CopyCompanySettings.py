#!/usr/bin/python
import sys
from subprocess import call


hostname="10.8.30.181"
username="c5235761"
getSettings1="/export/home/sfuser/sfv4-client/production/getCompanySettings.sh"
getSettings2="/app/sfv4client/getCompanySettings.sh"
 
def main():
    if len(sys.argv)<2 or len(sys.argv)>5:
        print "Usage ./CopyCompanySettings.py sourceCompany sourceEnv targetCompany targetEnv"
        sys.exit()
    else:
        global sourceCompany; sourceCompany=sys.argv[1]
        global sourceEnv; sourceEnv=sys.argv[2]
        global targetCompany; targetCompany=sys.argv[3]
        global targetEnv; targetEnv=sys.argv[4]
        global getCmpset
        getCmpset = "/app/apache-ant-1.8.2/bin/ant -f sfv4client.xml runclient -Dscript_class=\"com.successfactors.legacy.service.ejb.provisioning.ProvisioningClient\" -Dscript_args=\"-w bizx_app_provider -getAllFeatureIdsAndStatusForCompany -c %s -outfile CompanySettings_%s_$(hostname)_$(date +%%F).csv\""%(sourceCompany,sourceCompany)
        confirmation=raw_input("Confirm if the info is correct:\nsourceCompany:%s\nsourceEnv:%s\ntargetCompany:%s\ntargetEnv:%s\nType \"YES\" to continue\n"%(sourceCompany,sourceEnv,targetCompany,targetEnv))
        if confirmation.strip().lower()=="yes":
                getCompanySettings()
                
def getCompanySettings():
        getcmmd="ssh %s@%s \"sudo su -c \\\"cd /app/sfv4client && %s\\\" sfuser\""%(username,hostname,getCmpset)
        call(getcmmd,shell=True)

if __name__ == '__main__':
    main()
