import rpa as r

def click(xpath, s):
  if r.exist(xpath) & r.present(xpath):
    r.click(xpath)
    return s + 1
  else:
    print('Couldn\'t find'+xpath+' component')
    return s
