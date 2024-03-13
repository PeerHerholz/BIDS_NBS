import argparse
import os
from pathlib import Path


# define parser to collect required inputs
def get_parser():

    __version__ = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                    '_version.py')).read()

    class MaxListAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if len(values) > 2:
                raise argparse.ArgumentError(self, "maximum length of list is 2")
            setattr(namespace, self.dest, values)

    parser = argparse.ArgumentParser(description='a CLI for easing up the conversion from BIDS to BIDS-NBS datasets')
    parser.add_argument('bids_dir', action='store', type=Path, help='The directory where the to-be-updated BIDS-compliant dataset is stored.')
    parser.add_argument('nbs_files', help='NBS files to be used during metadata adaptation.', nargs='*', action=MaxListAction)
    parser.add_argument('--get_nbs_files',
                        help='Indicating if NBS metadata template files should be stored under sourcedata in the specified BIDS dataset'
                        'for subsequent metadata information denotation and usage during the conversion.')
    parser.add_argument('--new_bids_dir', action='store', type=Path, help='The directory where the new BIDS-NBS compliant dataset should be stored, in case metadata should not be changed in-place.')
    parser.add_argument('-v', '--version', action='version',
                        version='BIDS-NBS version {}'.format(__version__))
    return parser


# define the CLI
def run_bidsnbs():

    # get arguments from parser
    args = get_parser().parse_args()

    # special variable set in the container
    if os.getenv('IS_DOCKER'):
        exec_env = 'singularity'
        cgroup = Path('/proc/1/cgroup')
        if cgroup.exists() and 'docker' in cgroup.read_text():
            exec_env = 'docker'
    else:
        exec_env = 'local'


# run the CLI
if __name__ == "__main__":

    run_bidsnbs()
