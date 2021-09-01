# pulumi-aws-python-stack-references

Multiple Pulumi stacks on AWS using a single account and S3 state coded with Python

## Requirements

Install `pulumi` and `aws-vault` via `brew`. Add credentials with `aws-vault add` and reflect the name of the account below (Hint: after `exec`).

## Getting Started

1. Set Pulumi Passphrase:

    ```bash
    export PULUMI_CONFIG_PASSPHRASE="mysupersecretpassphrase"
    ````


1. Login to state:

    ```bash
    aws-vault exec me -- pulumi login s3://my-pulumi-state
    ```


1. Change directory to `bucket1` and install dependencies.

    ```bash
    cd bucket1
    ````


1. Create a new stack:

    ```bash
    aws-vault exec me -- pulumi stack init bucket1
    ```


1. Deploy everything:

    ```bash
    aws-vault exec me -- pulumi up
    ```

1. Change directory to `bucket2` and install dependencies.

    ```bash
    cd ../bucket2
    ````

1. Create a new stack:

    ```bash
    aws-vault exec me -- pulumi stack init bucket2
    ```

1. Deploy everything:

    ```bash
    aws-vault exec me -- pulumi up
    ```

1. Change directory to `served` and install dependencies.

    ```bash
    cd ../served
    ````

1. Create a new stack:

    ```bash
    aws-vault exec me -- pulumi stack init served
    ```

1. Deploy everything:

    ```bash
    aws-vault exec me -- pulumi up
    ```

## Clean Up

1. Once you are done, destroy all of the resources and the stack. Repeat this in each 
of the `bucket1`, `bucket2`, and `served` directories from above that you ran `pulumi up` within.

    ```bash
    $ pulumi destroy
    $ pulumi stack rm
    ```