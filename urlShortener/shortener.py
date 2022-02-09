"""
Create a URL Shortener in Python with pyshorteners library
Author: Shun Nagasaki
"""

import sys
import pyshorteners as pysh

def url_shortener(url):
  shortener = pysh.Shortener()
  return shortener.tinyurl.short(url)

def main():
  link = sys.argv[1]
  shortened = url_shortener(link)
  print(shortened)


if __name__ == '__main__':
  main()