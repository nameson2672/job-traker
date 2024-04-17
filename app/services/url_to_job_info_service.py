from urllib.parse import urlparse

from ..schemas import ScrapedJobInfo

from .job_info_by_url.indeed_url_parser_to_job_info_service import indeed_url_parser_to_job_info_service
from .job_info_by_url.linkedin_url_parser_to_job_info_service import linkedin_url_parser_to_job_info_service

# Dictionary mapping domain names to functions
domain_functions = {
    'www.linkedin.com': linkedin_url_parser_to_job_info_service,
    'www.indeed.com': indeed_url_parser_to_job_info_service,
}

def job_info_from_url(url) -> ScrapedJobInfo:
    # Parse the URL to extract the domain
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split(':')[0]

    # Get the appropriate function from the dictionary
    content_function = domain_functions.get(domain)

    # Call the function and return its result
    return linkedin_url_parser_to_job_info_service(url)