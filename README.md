# Azure-functionapps-demo

Simple demos of different Azure functions and durable functions. Different triggers and bindings are used for interacting with different Azure services. 

## Getting started
To start, check the following prerequisites:
* Azure function core tools (ideally v4.x). Install it  [func CLI installation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cmacos%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools) if not available yet.
```
func --version
```
* Azure CLI
```
az --version
```
* VS Code Azure Functions extension
* Python (ideally v3.7.x)
```
python --version
```
It is recommended to use a virtual environment, e.g. created by `conda`. To install, check [Miniconda installation](https://docs.conda.io/en/latest/miniconda.html)

## Simple functions
In the respository, there are different functions demonstrated using triggers and bindings interacting with:

* HTTP requests
* Azure blob storage 
* Azure table storage 
* Azure storage queue 

To start locally, configure the file of `template.local.settings.json` by specifying the storage account and app insights credentials and rename the file to `local.settings.json`.
After that simply input the below command while locating in the project root to trigger function hosting:
```
func start
```
And you should be able to see different functions hosted locally.

To deploy/publish it into Azure:
```
az login
func azure functionapp publish <Function-App-Name>
```

## Durable functions

There are also some examples of Azure durable functions and you can find them in the `DurableFunctions` folder. It contains demos of common durable function patterns including:
* Function chaing
* Fan-in/fan-out
* Async HTTP
* Monitoring
* Human interaction
* Durable entity (aggregator)

Start each of the function project locally after configurating the `local.settings.json`:
```
cd ./DurableFunctions/DurableFuncChaining
func start
```

## V2 Python programming model
In the `V2DemoFunctionProj` folder you can find another example demonstrating the newly introduced Azure functions Python V2 programming model. 
The main benefits of using the new model includes:
* Simplified folder structure
* Triggers and bindings defined as decorators, elimination of the usage of `function.json` files
* Introduction of `blue print` class for better importing behaviors