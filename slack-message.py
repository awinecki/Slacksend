import sys
import argparse
from workflow import Workflow, ICON_WEB, web, PasswordNotFound
import urllib

def main(wf):

    parser = argparse.ArgumentParser()
    parser.add_argument('--setkey', dest='apikey', nargs='?', default = None)
    parser.add_argument('query', nargs='?', default = None)
    args = parser.parse_args(wf.args)

    if args.apikey:
        wf.save_password('slack_api_key', args.apikey)
        return 0

    try:
        api_key = wf.get_password('slack_api_key')
        print api_key
    except PasswordNotFound:
        wf.add_item('No API key set.',
            'Please run slt',
            valid = False)
        wf.send_feedback()
        return 0

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    channel = '#working-on'
    channel_safe = urllib.quote(channel)
    query = '_' + query + '_'
    query_safe = urllib.quote(query, '')

    web.get('https://slack.com/api/chat.postMessage?token=' +
        'xoxp-2312755488-2312755490-4627716458-c9be87&channel=' +
        channel_safe + '&text=' + query_safe + '&as_user=true&pretty=1')

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

