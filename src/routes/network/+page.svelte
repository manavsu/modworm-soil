<script lang="ts">
    import "$lib/app.css";
    import Title from "$lib/title.svelte";
    import { BASE_URL } from "$lib/env";
    import { fade } from 'svelte/transition';
    import { Network, Socket } from "$lib/network";
    import NetworkView from "./network_view.svelte";
    import { onMount } from "svelte";
    import { Working, ConnectedSocket} from "$lib/store";

    let cidr = "";
    let ports = "";
    let error: string | null;
    let scanning = false;
    let selected_network: Network | null = null;

    let Networks: Network[] = [];

    $: Working.set(scanning);

    async function GetNetworks() {
        const response = await fetch(`${BASE_URL}/get/networks/`);
        if (!response.ok) {
            error = await response.json().then(r => r.error);
            return;
        }
        error = null;
        return await response.json();
    }

    async function GetSavedNetworks() {
        let json_networks = null;
        try {
            json_networks = await GetNetworks();
        } catch (e) {
            if (e instanceof Error) {
                error = e.message;
            } else {
                error = "An unknown error occurred.";
            }
        }
        if (json_networks) {
            Networks = json_networks.map((network: any) => new Network(network.cidr, network.ports, network.open_sockets));
            console.log(Networks)
        }
    }

    async function NetworkMap(cidr:string, port:string) {
        const response = await fetch(`${BASE_URL}/nmap/${cidr}/${port}`);
        if (!response.ok) {
            error = await response.json().then(r => r.error);
            return;
        }
        error = null;
        return await response.json();
    }

    async function HandleSubmit(cidr_t:string, ports_t:string) {
        if (scanning) return
        scanning = true

        cidr = cidr_t || "127.0.0.1"
        ports = ports_t || "-"

        const parsed_cidr = cidr.replace("/", "+")
        let json_network = null;
        try {
            json_network = await NetworkMap(parsed_cidr, ports)
        } catch (e) {
            if (e instanceof Error) {
                error = e.message;
            } else {
                error = "An unknown error occurred.";
            }
        }
        if (json_network) {
            const matching_network = Networks.find(network => network.cidr === cidr && network.ports === ports);
            if (matching_network) {
                matching_network.open_sockets = new Network(cidr, ports, json_network).open_sockets;
            } else {
                Networks.push(new Network(cidr, ports, json_network));
            }
        }

        await new Promise(r => setTimeout(r, 500))
        Networks = [...Networks]
        scanning = false
        console.log(Networks)
        console.log(selected_network)
    }

    function GetHeight(network: Network) {
        if (network.open_sockets.length == 0) return 1;
        if (network.open_sockets.length == 1 && network.cidr == network.open_sockets[0].address && network.ports == network.open_sockets[0].port) return 1;
        return (network.open_sockets.length + 1 - Math.floor(network.open_sockets.length / 3));
    }

    function RemoveNetwork(index: number) {
        Networks = Networks.filter((_, i) => i !== index);
    }

    function OnConnect(socket: Socket) {
        ConnectedSocket.set(socket);
        console.log($ConnectedSocket)
    }

    function OnScan(index: number) {
        HandleSubmit(Networks[index].cidr, Networks[index].ports)
    }

    onMount(() => {
        GetSavedNetworks();
    });
</script>

<div in:fade={{delay: 200, duration:200}} class="flex flex-col">
    <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2 p-2">
            {#if !error}
                <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                    <Title>Networks</Title>
                    </div>
                {:else}
            <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                    <h2 class="text-center text-xl text-rose-900">{error}</h2>
                </div>
            {/if}
    </div>
    <div class="transition-all duration-500 ease-in-out grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 grid-flow-dense gap-0">

        <div class="row-span-2 p-2">
            <div in:fade={{delay: 200, duration:200}} class="flex flex-col border-2 border-gray-600 rounded-xl justify-center w-full py-6 min-w-fit">
                <form class="flex flex-row w-fit mx-auto items-center {scanning ? 'text-gray-500' : ''}">
                    <div class="flex flex-col">
                        <div class="flex flex-row border-2 rounded-md input px-2 py-1 mb-3 mr-2 ml-3 {scanning ? 'border-gray-500' : 'border-white'}">
                            <input type="text" class="bg-transparent focus:outline-none pr-1 w-full" bind:value={cidr} placeholder="127.0.0.1" disabled={scanning}>
                            <p>CIDR</p>
                        </div>
                        <div class="flex flex-row border-2 rounded-md input px-2 py-1 mr-2 ml-3 {scanning ? 'border-gray-500' : 'border-white'}">
                            <input type="text" class="bg-transparent focus:outline-none pr-1 w-full" bind:value={ports} placeholder="-" disabled={scanning}>
                            <p>Ports</p>
                        </div>
                    </div>

                    <p class="text-3xl transform duration-300">&#9675;</p>

                    <button on:click={() => HandleSubmit(cidr, ports)} class="border-2 px-2 py-1 m-3 clickable w-32 {scanning ? 'border-gray-500' : 'border-white'}" disabled={scanning}>Scan</button>
                </form>
            </div>
        </div>

        {#if Networks.length > 0}
            {#each Networks as network, index}
                <div in:fade={{delay: 200, duration:200}} style="grid-row-end: span {GetHeight(network)}" class="flex flex-col justify-center p-2">
                    <NetworkView network={network} remove={() => RemoveNetwork(index)} connect={(socket) => OnConnect(socket)} scan={() => OnScan(index)} scanning={scanning}/>
                </div>
            {/each}
        {/if}

    </div>
</div>


