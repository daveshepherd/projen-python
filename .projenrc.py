from projen_jsii import PythonPackage

project = PythonPackage(
    author_email="dave.shepherd@unibuddy.com",
    author_name="Dave Shepherd",
    module_name="projen_python",
    name="projen-python",
    version="0.1.0",
    deps=["../projen-jsii/dist/python/projen_jsii-0.0.0.tar.gz"],
)

project.synth()