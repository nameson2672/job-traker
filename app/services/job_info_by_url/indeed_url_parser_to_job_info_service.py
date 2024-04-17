def indeed_url_parser_to_job_info_service(soup):
    job_title = soup.find('h1', class_='jobsearch-JobInfoHeader-title').get_text().strip()
    company_name = soup.find('div', class_='icl-u-lg-mr--sm icl-u-xs-mr--xs').get_text().strip()
    location = soup.find('div', class_='jobsearch-InlineCompanyRating').get_text().strip()
    description = soup.find('div', class_='jobsearch-JobComponent-description icl-u-xs-mt--md').get_text().strip()

    job_info = {
        'job_title': job_title,
        'company_name': company_name,
        'location': location,
        'description': description
    }

    return job_info
