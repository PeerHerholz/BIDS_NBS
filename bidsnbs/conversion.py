import os
import seedir as sd
import json
from shutil import copy
from bidsnbs.utils import check_path


def add_nbs_file_metadata_subject_events_json(events_json, nbs_file_events, bids_dir, sub_id):
    """
    Add NBS metadata from templates to existing events.json files.

    Parameters
    ----------
    events_json : str or PosixPath
        A string or PosixPath indicating the path to the existing events.json file.
    nbs_file_events : str or PosixPath
        A string or PosixPath indicating the path to the NBS events metadata file.

    Returns
    -------
    Updated events metadata.

    Examples
    --------
    Add NBS metadata from templates to existing events.json files.

    >>>add_nbs_file_metadata_subject_events_json('/home/user/BIDS_dataset/sub-01/eeg/sub-01_task-rest_events.json',
                                                 '/home/user/BIDS_dataset/sourcedata/BIDS_NBS_templates/nbs_template_events.json')
    """

    # open both json files
    with open(events_json, 'r') as events_json_nbs:
        events_json_nbs_data = json.load(events_json_nbs)

    with open(nbs_file_events, 'r') as nbs_file_events_tpl:
        nbs_file_events_tpl_data = json.load(nbs_file_events_tpl)
    
    # copy existing events.json to sourcedata as a backup
    if 'ses-' in events_json:
        ses_s = events_json.find('ses-')+4
        ses_e = events_json.find('/', ses_s)
        ses_id = events_json[ses_s: ses_e]
        sub_bu_path = str(bids_dir) + '/sourcedata/BIDS_pre_NBS_backup/sub-%s/ses-%s/' % (sub_id, ses_id)
    else:
        sub_bu_path = str(bids_dir) + '/sourcedata/BIDS_pre_NBS_backup/sub-%s/' % sub_id

    check_path(sub_bu_path)
    copy(events_json, sub_bu_path + events_json.split('/')[-1])
    os.remove(events_json)

    # add template metadata to existing events.json
    events_json_nbs_data.update(nbs_file_events_tpl_data)
    
    # overwrite existing events.json file with updated data
    with open(events_json, 'w') as output_file:
        json.dump(events_json_nbs_data, output_file, indent=4)

    return events_json_nbs_data
