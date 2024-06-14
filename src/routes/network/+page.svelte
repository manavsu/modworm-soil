<script lang="ts">
    import "$lib/app.css";
    import Title from "$lib/title.svelte";
    import { BASE_URL } from "$lib/env";
    import { fade } from 'svelte/transition';
    import { Network, Socket } from "$lib/network";
    import NetworkView from "./network_view.svelte";
    import { Working } from "$lib/store";

    let cidr = "";
    let ports = "";
    let error: string | null;
    let scanning = false;
    let selected_network: Network | null = null;

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

    async function HandleSubmit(cidr_t:string, ports_t:string) {
        if (scanning) return
        scanning = true

        cidr = cidr_t || "127.0.0.1"
        ports = ports_t || "502"

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
        await new Promise(r => setTimeout(r, 500))
        scanning = false
        console.log(Networks)
        console.log(selected_network)
    }

    function GetHeight(network: Network) {
        if (network.open_sockets.length == 0) return 1;
        if (network.open_sockets.length == 1 && network.cidr == network.open_sockets[0].address && network.ports == network.open_sockets[0].port) return 1;
        return (network.open_sockets.length + 1 - Math.floor(network.open_sockets.length / 3));
    }
</script>

<div class="flex flex-col">
    <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2">
        <Title>Network</Title>
    </div>
    <div class="grid grid-cols-3 grid-flow-dense gap-0">

        <div class="row-span-2 p-2">
            <div class="flex flex-col border-2 border-gray-600 rounded-xl justify-center w-full py-6">
                <form in:fade={{delay: 200, duration:200}} out:fade={{duration:200}} class="flex flex-row w-fit mx-auto items-center {scanning ? 'text-gray-500' : ''}">
                    <div class="flex flex-col">
                        <div class="flex flex-row border-2 rounded-md input px-2 py-1 mb-3 mr-2 {scanning ? 'border-gray-500' : 'border-black dark:border-white'}">
                            <input type="text" class="bg-transparent focus:outline-none w-20 md:w-40 pr-1" bind:value={cidr} placeholder="127.0.0.1" disabled={scanning}>
                            <p>CIDR</p>
                        </div>
                        <div class="flex flex-row border-2 rounded-md input px-2 py-1 mr-2 {scanning ? 'border-gray-500' : 'border-black dark:border-white'}">
                            <input type="text" class="bg-transparent focus:outline-none w-20 md:w-40 pr-1" bind:value={ports} placeholder="502" disabled={scanning}>
                            <p>Ports</p>
                        </div>
                    </div>
                    <p class="text-3xl transform duration-300">&#9675;</p>
                    <button on:click={() => HandleSubmit(cidr, ports)} class="border-2 px-2 py-1 ml-3 clickable w-32 {scanning ? 'border-gray-500' : 'border-black dark:border-white'}" disabled={scanning}>Scan</button>
                    {#if error}
                        <h2 transition:fade class="text-center text-fuchsia-500 dark:text-fuchsia-800">{error}</h2>
                    {/if}
                </form>
            </div>
        </div>

        {#if Networks.length > 0}
            {#each Networks as network}
                <div style="grid-row-end: span {GetHeight(network)}" class="flex flex-col justify-center p-2">
                    <NetworkView network={network} />
                </div>
            {/each}
        {/if}

    </div>
</div>


