#!/usr/bin/env python
import yea


def main():
    # import here so we can profile how long it takes
    import wandb

    run = wandb.init()
    wandb.log(dict(this=2))
    run.finish()


if __name__ == "__main__":
    yea.setup()
    main()
