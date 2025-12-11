import argostranslate.package
argostranslate.package.update_package_index()
available = argostranslate.package.get_available_packages()
pkg = next(filter(lambda x: x.from_code == 'en' and x.to_code == 'pt', available), None)
if pkg:
    argostranslate.package.install_from_path(pkg.download())
print("Done!")
