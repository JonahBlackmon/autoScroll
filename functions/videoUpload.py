import time
import os
import requests
import json
from functions.pathConfig import get_default
from functions.captions import generate_caption

default_path = get_default()

def ig_upload(responses):
    for response in responses:
        pageID = os.getenv('IG_PAGEID')

        ig_user_id = os.getenv('IG_USERID')

        access_token = os.getenv('INSTAGRAM_TOKEN')

        video_url = response
        
        def upload_video(video_url, access_token, ig_user_id) :
            
            caption = generate_caption()
            post_url = 'https://graph.facebook.com/v18.0/{}/media'.format(ig_user_id)
            payload = {
                'media_type' : 'REELS',
                'video_url' : video_url,
                'caption': caption,
                'access_token' : access_token
            }
            r = requests.post(post_url, data=payload)
            print(r.text)
            results = json.loads(r.text)
            return(results)

        def status_code(ig_container_id, access_token) :
            graph_url = 'https://graph.facebook.com/v18.0/'
            url = graph_url + ig_container_id
            param = {}
            param['access_token'] = access_token
            param['fields']='status_code'
            response = requests.get(url, params=param)
            response = response.json()
            return(response['status_code'])

        def publish_video(results, access_token):
            if 'id' in results:
                creation_id = results['id']
                second_url = 'https://graph.facebook.com/v18.0/{}/media_publish'.format(ig_user_id)
                second_payload = {
                    'creation_id':creation_id,
                    'access_token':access_token
                }

                r = requests.post(second_url, data=second_payload)
                print(r.text)
                print('video published to instagram')
            else:
                print('video posting is not possible')

        results=upload_video(video_url, access_token, ig_user_id)
        print('please wait for some time')
        time.sleep(10)

        ig_container_id=results['id']
        s=status_code(ig_container_id, access_token)

        if s == 'FINISHED':
            print('video uploaded successfully')
            publish_video(results, access_token)
        else:
            print('still wait for some time')
            time.sleep(60)
            publish_video(results, access_token)
            