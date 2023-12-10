import typer
import yaml
from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg


def scrap_read(device, chapter):
    with Scrapli(**device) as conn:
        cfg_conn = ScrapliCfg(conn=conn)
        cfg_conn.ignore_version = True
        config = cfg_conn.get_config()
        with open(f"{chapter}/backups/{device['host']}.cfg", "w") as f:
            f.writelines(config.result)
    


def main(chapter: str):
    with open(f"{chapter}/bgp.clab.yaml") as f:
        data = yaml.safe_load(f)
        nodes = data["topology"]["nodes"]
        for k, v in nodes.items():
            device = {
                "host": k,
                "auth_username": "admin",
                "auth_password": "admin",
                "auth_strict_key": False,
                "platform": "arista_eos"
            }
            scrap_read(device, chapter)


if __name__ == "__main__":
    typer.run(main)
