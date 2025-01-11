from typing import List

from app.models.organizations import Activity


def collect_inner_activity_ids(activity: Activity) -> List[int]:
    activity_ids = [
        activity.id,
    ]
    if activity.inner_activities:
        for activity in activity.inner_activities:
            activity_ids.extend(collect_inner_activity_ids(activity))

    return activity_ids
