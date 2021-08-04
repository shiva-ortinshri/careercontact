import pandas as pd

pre = pd.read_pickle('data/preevent_responses.pandas')
post = pd.read_pickle('data/postevent_responses.pandas')

pre_expanded = pd.DataFrame()
for ind, row in pre.iterrows(): # this is slow and there's probably a better way
    events = row.events.split(',')
    for e in events:
        row.loc['event'] = e
        pre_expanded = pre_expanded.append(row, ignore_index=True)

responses_joint = pd.merge(pre_expanded, post, on=['email', 'event'], suffixes=('_pre', '_post'))

responses_joint.to_pickle('data/matched_responses.pandas')
pre_expanded.to_pickle('data/preevent_responses_expanded.pandas')