<script lang="ts">
    import "$lib/app.css";
    import Title from "$lib/title.svelte";
    import { BASE_URL } from "$lib/env";
    import { fade } from 'svelte/transition';
    import { Network, Socket } from "$lib/network";
    import LoadingSnake from "$lib/loading_snake.svelte";
    import { Working } from "$lib/store";

    let cidr = "";
    let ports = "";
    let error: string | null;
    let scanning = false;
    let adding = false;

    let Networks: Network[] = [];

    $: Working.set(scanning);

    async function NetworkMap(cidr:string, port:string) {
        const response = await fetch(`${BASE_URL}/nmap/${cidr}/${port}`);
        if (!response.ok) {
            error = await response.json().then(r => r.error);
            return;
        }
        error = null;
        const servers = await response.json();
        return servers;
    }

    async function HandleSubmit() {
        if (scanning) return
        scanning = true

        cidr = cidr || "127.0.0.1"
        ports = ports || "502"

        const parsed_cidr = cidr.replace("/", "+")
        const json_network = await NetworkMap(parsed_cidr, ports)
        if (json_network) {
            const matching_network = Networks.find(network => network.cidr === cidr && network.ports === ports);
            if (matching_network) {
                matching_network.open_sockets = new Network(cidr, ports, json_network).open_sockets;
            } else {
                Networks.push(new Network(cidr, ports, json_network));
            }
        }
        Networks = [...Networks]
        scanning = false
        console.log(Networks)
    }

    function HandleAdd() {
        adding = true;
    }

    function HandleCancel() {
        adding = false;
    }
</script>

    <div class="mx-auto">
        <Title>Network</Title>
    </div>

    <div class="flex flex-row flex-grow border">
        <div class="flex flex-col w-1/3 border justify-center">
            <form in:fade={{delay: 200, duration:200}} out:fade={{duration:200}} class="flex flex-col text-sm w-fit mx-auto {scanning ? 'text-gray-500' : ''}">
                <div class="flex flex-row border-2 rounded-md input px-2 py-1 mb-3 {scanning ? 'border-gray-500' : 'border-black dark:border-white'}">
                    <input type="text" class="bg-transparent focus:outline-none pr-1" bind:value={cidr} placeholder="127.0.0.1" disabled={scanning}>
                    <p>CIDR</p>
                </div>
                <div class="flex flex-row border-2 rounded-md input px-2 py-1 mb-3 {scanning ? 'border-gray-500' : 'border-black dark:border-white'}">
                    <input type="text" class="bg-transparent focus:outline-none pr-1" bind:value={ports} placeholder="502" disabled={scanning}>
                    <p>Ports</p>
                </div>
                <button on:click={HandleSubmit} class="border-2 px-2 py-1 clickable mb-3 {scanning ? 'border-gray-500' : 'border-black dark:border-white'}" disabled={scanning}>
                    {#if !scanning} Scan {:else} Scanning... {/if}
                </button>
                {#if error}
                        <h2 transition:fade class="text-center text-fuchsia-500 dark:text-fuchsia-800">{error}</h2>
                {/if}
            </form>
        </div>

        {#each Networks as network}
            <div class="flex flex-col p-2 mb-3">
                <p>{network.cidr} : {network.ports}</p>
                {#each network.open_sockets as socket}
                    <p>{socket.address} : {socket.port}</p>
                {/each}
            </div>
        {/each}
    </div>

