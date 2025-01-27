from datetime import datetime

from tqdm import tqdm
from wagtail.rich_text import RichText
from content_migration.management.shared import parse_csv_file

from events.models import Event, EventsIndexPage

# Event dates are in ISO 8601 format
date_format = "%Y-%m-%dT%H:%M:%S%z"


def handle_import_events(file_name: str) -> None:
    # Get the only instance of Magazine Department Index Page
    events_index_page = EventsIndexPage.objects.get()

    events_list = parse_csv_file(file_name)

    for event in tqdm(events_list, desc="events", unit="row"):
        event_exists = Event.objects.filter(
            drupal_node_id=event["drupal_node_id"],
        ).exists()

        if not event_exists:
            # Convert event date strings into Python dates
            start_date = datetime.strptime(event["start_date"], date_format)
            end_date = datetime.strptime(event["end_date"], date_format)

            # Get teaser, max length is 100 characters
            teaser = None
            if event["body"]:
                teaser = event["body"][0:99]

            event_body_blocks = []
            # Create rich text block for event body blocks list
            rich_text_block = ("rich_text", RichText(event["body"]))
            event_body_blocks.append(rich_text_block)

            import_event = Event(
                title=event["title"],
                body=event_body_blocks,
                teaser=teaser,
                start_date=start_date,
                end_date=end_date,
                website=event["event_link"],
                category=Event.EventCategoryChoices.WESTERN,
            )

            # # Add event to site page hiererchy
            events_index_page.add_child(instance=import_event)
            events_index_page.save()
