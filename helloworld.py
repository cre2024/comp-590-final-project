from mpyc.runtime import mpc

async def main():
    await mpc.start()     # connect to all other parties
    print(''.join(await mpc.transfer('Hello world!')))
    await mpc.shutdown()  # disconnect, but only once all other parties reached this point

if __name__ == '__main__':
    mpc.run(main())