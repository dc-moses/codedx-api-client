import argparse

from codedx_api import CodeDx

# API key and base url from Code DX
parser = argparse.ArgumentParser()
parser.add_argument('base_url', type=str, help='Base URL for Code DX: https://HOST/codedx')
parser.add_argument('api_key', type=str, help='API from Code DX')
parser.add_argument('project', type=str, help='Code DX project name or id')
args = parser.parse_args()

cdx = CodeDx.CodeDx(args.base_url, args.api_key)

res = cdx.get_pdf(args.project)
