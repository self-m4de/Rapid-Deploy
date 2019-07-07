import argparse
import do_get_account
import do_ssh_keys
import add_ssh_key
import do_get_droplet
import create_droplet
import do_get_images
import do_get_snapshots
import delete_droplet

#   TODO
#   Create droplet - functionality to be able to select image
#   Ensure that all help information is sufficient

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--account', help='Get account info', action='store_true')
parser.add_argument('-k', '--key', help='Get ssh key info', action='store_true')
parser.add_argument('-K', '--Key', help='Add ssh key')
parser.add_argument('-d', '--droplet', help='Get droplet info', action='store_true')
parser.add_argument('-c', '--create', help='Create new droplet')
parser.add_argument('-C', '--multiple', help='Create multiple droplets')
parser.add_argument('-i', '--images', help='List images', action='store_true')
parser.add_argument('-s', '--snapshots', help='List snapshots', action='store_true')
parser.add_argument('-D', '--destroy', help='Destroy a droplet\trapid_deploy.py -D <id>', action='store_true')

args = parser.parse_args()

if args.account:
    account_info = do_get_account.get_account_info()

    if account_info is not None:
        print("Here's your info: ")
        for k, v in account_info['account'].items():
            print('{0}:{1}'.format(k, v))

    else:
        print('[!] Request Failed')

if args.key:
    ssh_keys = do_ssh_keys.get_ssh_keys()

    if ssh_keys is not None:
        print('Here are your keys: ')
        for key, details in enumerate(ssh_keys['ssh_keys']):
            print('Key {}:'.format(key))
            for k, v in details.items():
                print(' {0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')

if args.Key is not None:
    add_response = add_ssh_key.add_ssh_key('test_file', arg.Key)

    if add_response is not None:
        print('Your key was added: ')
        for k, v in add_response.items():
            print('  {0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')

if args.droplet:
    droplet_info = do_get_droplet.get_droplet_info()

    if droplet_info:
        for key, details in enumerate(droplet_info['droplets']):
            print('Droplet {}:'.format(key))
            for k, v in details.items():
                print(' {0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')

if args.create is not None:
    create_droplet.create_new_droplet(args.create)

if args.destroy:
    droplet_id = input("Enter the droplet ID to delete.\n\tIf unsure, run rapid_deploy -d first\n")
    delete_droplet.destroy_droplet(droplet_id)

if args.multiple is not None:
    base = args.multiple
    create_list = []
    num = input("How many droplets would you like to create?\n")
    for x in range (0, int(num)):
        name = base + str(x+1)
        create_list.append(name)
        create_droplet.create_new_droplet(create_list[x])

if args.images:
    images = do_get_images.get_images()

    if images:
        for k, v in enumerate(images['images']):
            print(' {0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')

if args.snapshots:
    snapshots = do_get_snapshots.get_snapshots()

    if snapshots:
        for k, v in enumerate(snapshots['snapshots']):
            print('Snapshot {0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')
