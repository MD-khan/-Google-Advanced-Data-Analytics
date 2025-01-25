def id_validator(verified_ids, feedback_ids):
    unverified_ids = []
    for feedback_id in feedback_ids:
        if feedback_id not in verified_ids:
            unverified_ids.append(feedback_id)
    total_ids = len(feedback_ids)
    unverified_count = len(unverified_ids)
    percentage_unverified = (unverified_count / total_ids) * 100
    print(f"{unverified_count} of {total_ids} IDs unverified.")
    print(f"{percentage_unverified:.2f}% unverified.")
id_validator(verified_ids=['1', '2'], feedback_ids=['1', '2', '3'])