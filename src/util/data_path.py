from furl import furl

repoUrl = "https://github.com/zakdances/housing-element-shapefiles/tree/main"

def data_path(county, municipality, as_url=False, parse_url=False):
    path = f"counties/{county}/cities/{municipality}"
    if as_url:
        path = f"{repoUrl}/{path}"
        if parse_url:
            path = furl(path).url
            # print(path)
    return path