<script lang="ts">
    import Title from '$lib/title.svelte';
    import { ConnectedSocket, Working } from '$lib/store';
    import { fade } from 'svelte/transition';
    import { BASE_URL } from '$lib/env'; 
    import LoadingSnake from '$lib/loading_snake.svelte';
    import Table from './table.svelte';
    
    let coil_table: []|null;
    let discrete_input_table: []|null;
    let holding_registers_table: []|null;
    let input_registers_table: []|null;
    
    async function GetDeviceInfo() {
        
    }

    async function ScanTable(ip:string, port:string, table:number) {
        if ($ConnectedSocket == null) return;
        $Working = true;
        const response = await fetch(`${BASE_URL}/mmap/table/${ip}/${port}/${table}/`);
        if (!response.ok) {
            $Working = false;
            return await response.json();
        }
        const table_list = await response.json();
        $Working = false;
        return table_list;
    }

    async function ScanAllTables(address:string, port:string) {
        holding_registers_table = (await ScanTable(address, port, 3)).holding_registers;
        coil_table = (await ScanTable(address, port, 1)).coils;
        discrete_input_table = (await ScanTable(address, port, 2)).discrete_inputs;
        input_registers_table = (await ScanTable(address, port, 4)).input_registers;
    }

    $: if ($ConnectedSocket != null) (async () => await ScanAllTables($ConnectedSocket.address, $ConnectedSocket.port))();
</script>

<div in:fade={{delay: 200, duration:200}} class="flex flex-col h-full">
    <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2 p-2">
        <Title>Tables</Title>
    </div>
    {#if $ConnectedSocket == null}
        <div class="flex flex-col justify-center items-center flex-grow text-2xl">
            <p>No connected socket, scan and connect from the networks page.</p>
            <a href="/network" class="border-2 px-10 py-2 mt-8 clickable border-white text-center">Networks</a>
        </div> 
    {:else}
        <div class="flex flex-row flex-wrap mx-auto p-2 w-full justify-around h-full">
            <div class="w-1/4 mx-auto border"><Table table={coil_table}/></div>
            <div class="w-1/4 mx-auto border"><Table table={discrete_input_table}/></div>
            <div class="w-1/4 mx-auto border"><Table table={holding_registers_table}/></div>
            <div class="w-1/4 mx-auto border"><Table table={input_registers_table}/></div>
        </div>
    {/if}
</div>
