"""
The task of the job processor is to take a JSON description
of a new job, send the message to the analyzer and post the
results to firebase.
"""

import analyzer.engine

def process_job(job_json, fb_uploader, es_uploader):
    """
    Given a JSON belonging to a job, process_job sends it to the
    analyzer and then it posts the output to firebase and
    elasticsearch.
    """
    print('Processing message: ' + job_json['message'])
    analysis_result = analyzer.engine.nlp_analysis(job_json)
    print('Send results to firebase')
    job_json['analysis'] = analysis_result
    fb_uploader.upload_analysis(job_json)
    print('Send results to elasticsearch')
    es_uploader.upload_analysis(job_json)
    return True
