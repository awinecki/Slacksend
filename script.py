import sys

from workflow import Workflow


def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`
    # Your imports here if you want to catch import errors
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    import somemodule
    import anothermodule
    # Get args from Workflow, already in normalised Unicode
    args = wf.args

    # Do stuff here ...

    # Add an item to Alfred feedback
    wf.add_item(u'Item title', u'Item subtitle')

    # Send output to Alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
