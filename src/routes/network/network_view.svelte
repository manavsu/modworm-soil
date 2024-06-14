<script lang="ts">
    import { Network } from "$lib/network";
    import { fade } from 'svelte/transition';
    export let network: Network;
    export let remove: () => void;
    export let connect: () => void;
    export let scan: () => void;
    export let scanning: boolean;
</script>

{#if network.open_sockets.length == 1 && network.cidr == network.open_sockets[0].address && network.ports == network.open_sockets[0].port}
    <div class="flex flex-row p-2 justify-between rounded-xl mx-auto items-center border-2 w-full border-gray-600 h-14">
        <p class="text-xl">{network.cidr} : {network.ports}</p>
        <div class="flex flex-row">
            <button on:click={connect} class="py-1 px-5 hover:scale-110 transition duration-300 rounded-xl border-2 place-items-center">Connect</button>
            <button on:click={remove} class="py-1 px-3 ml-2 hover:scale-110 transition duration-300 rounded-xl border-2 place-items-center">×</button>
        </div>
    </div>
{:else if network.open_sockets.length > 0}
    <div class="flex flex-col p-2 rounded-xl border-2 w-full border-gray-600">
        <div class="flex flex-row justify-between items-center w-full pb-3 pt-1 mx-auto">
            <p class="text-xl">{network.cidr} : {network.ports}</p>
            <div class="flex flex-row">
                <button on:click={scan} class="py-1 px-2 hover:scale-110 transition duration-300 rounded-xl border-2 place-items-center {scanning ? 'border-gray-500 text-gray-500' : 'border-white'}" disabled={scanning}>Scan</button>
                <button on:click={remove} class="py-1 px-3 ml-2 hover:scale-110 transition duration-300 rounded-xl border-2 place-items-center">×</button>
            </div>
        </div>
        {#each network.open_sockets as socket}
            <hr class="w-full text-white mx-auto"/>
            <div class="flex flex-row w-full justify-between py-2 items-center">
                <p>{socket.address} : {socket.port}</p>
                <button on:click={connect} class="px-5 py-1 hover:scale-110 transition duration-300 rounded-xl border-2 place-items-center">Connect</button>
            </div>
        {/each}
    </div>
{:else}
    <div class="flex flex-row p-2 justify-between rounded-xl mx-auto items-center border-2 w-full border-rose-900 h-14">
        <p class="text-xl text-rose-900">{network.cidr} : {network.ports}</p>
        <div class="flex flex-row">
            <button on:click={scan} class="text-rose-900 py-1 px-2 hover:scale-110 transition duration-300 rounded-xl border-2 border-rose-900 place-items-center {scanning ? 'border-rose-950 text-rose-950' : 'border-rose-900'}" disabled={scanning}>Scan</button>
            <button on:click={remove} class="text-rose-900 py-1 px-3 ml-2 hover:scale-110 transition duration-300 rounded-xl border-2 border-rose-900 place-items-center">×</button>
        </div>
    </div>
{/if}