#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import hashlib
import requests
import json


class WecomBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={api_key}"
        self.headers = {'Content-Type': 'application/json'}

    def _get_file_base64(self, file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()
            return base64.b64encode(file_content).decode('utf-8')

    def _get_file_md5(self, file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def _handle_response(self, response):
        try:
            data = response.json()
            if data.get("errcode") == 0:
                return True, data.get("errmsg", "Success")
            else:
                return False, data.get("errmsg", "Unknown error")
        except ValueError:
            return False, "Invalid JSON response"

    def send_text(self, content, **kwargs):
        valid_params = {'mentioned_list', 'mentioned_mobile_list'}
        invalid_params = set(kwargs) - valid_params
        if invalid_params:
            return False, f'Invalid parameters: {invalid_params}'
        payload = {"msgtype": "text", "text": {"content": content}}
        payload['text'].update(kwargs)

        try:
            response = requests.post(
                self.url, headers=self.headers, data=json.dumps(payload)
            )
            response.raise_for_status()
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return False, str(e)

    def send_image(self, image_path):
        try:
            base64_data = self._get_file_base64(image_path)
            md5_data = self._get_file_md5(image_path)
        except IOError as e:
            return False, str(e)

        payload = {
            "msgtype": "image",
            "image": {"base64": base64_data, "md5": md5_data},
        }

        try:
            response = requests.post(
                self.url, headers=self.headers, data=json.dumps(payload)
            )
            response.raise_for_status()  # 检查HTTP状态码
            return self._handle_response(response)

        except requests.exceptions.RequestException as e:
            return False, str(e)
