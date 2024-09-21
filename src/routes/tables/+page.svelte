<script lang="ts">
    import Title from '$lib/title.svelte';
    import { ConnectedSocket, Working, CurrentTable} from '$lib/store';
    import { fade } from 'svelte/transition';
    import { BASE_URL } from '$lib/env'; 
    import LoadingSnake from '$lib/loading_snake.svelte';
    import Table from './table.svelte';
    import type { TableStore } from '$lib/modbus_table';
    import { ModbusTable } from '$lib/modbus_table';
    
    let coil_table: number[][]|null;
    let discrete_input_table: number[][]|null;
    let holding_registers_table: number[][]|null;
    let input_registers_table: number[][]|null;

    let device_info: any | null;
    let error: string | null = null;
    
    async function GetDeviceInfo(address:string, port:string, hard:boolean=false) {
        if ($ConnectedSocket == null) return;
        $Working = true;
        const response = await fetch(`${BASE_URL}/deviceinfo/${address}/${port}/`);
        if (!response.ok) {
            $Working = false;
            throw new Error(await response.text());
        }
        device_info = await response.json();
        $Working = false;
    }

    async function ScanTable(ip:string, port:string, table:number, hard:boolean = false) {
        if ($ConnectedSocket == null) return;
        $Working = true;
        const response = await fetch(`${BASE_URL}/mmap/table/${ip}/${port}/${table}/${hard ? 1 : 0}/`);
        if (!response.ok) {
            $Working = false;
            throw new Error(await response.text());
        }
        const table_list = await response.json();
        $Working = false;
        return table_list;
    }

    async function ScanAllTables(address:string, port:string, hard:boolean = false) {
        try {
            coil_table = (await ScanTable(address, port, 1, hard));
            discrete_input_table = (await ScanTable(address, port, 2, hard));
            holding_registers_table = (await ScanTable(address, port, 3, hard));
            input_registers_table = (await ScanTable(address, port, 4, hard));
            await GetDeviceInfo(address, port, hard);
        } catch (e: any) {
            error = e.message;
        }

    }

    async function Refresh() {
        coil_table = null;
        discrete_input_table = null;
        holding_registers_table = null;
        input_registers_table = null;
        device_info = null;
        if ($ConnectedSocket == null) return;
        await ScanAllTables($ConnectedSocket.address, $ConnectedSocket.port, true);
    }

    $: if ($ConnectedSocket != null) (async () => await ScanAllTables($ConnectedSocket.address, $ConnectedSocket.port, false))();
</script>

<div in:fade={{delay: 200, duration:200}} class="flex flex-col h-full">
    <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2 p-2">
        {#if !error}
            <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                <Title>Tables</Title>
            </div>
        {:else}
            <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                <h2 class="text-center text-xl text-rose-900">{error}</h2>
            </div>
        {/if}
    </div>
    {#if $ConnectedSocket == null}
        <div class="flex flex-col justify-center items-center flex-grow text-2xl">
            <p class="text-center">No connected socket, scan and connect from the networks page.</p>
            <a href="/" class="border-2 px-10 py-2 mt-8 clickable border-white text-center">Networks</a>
        </div> 
    {:else}
        <div class="border-2 border-gray-600 rounded-xl m-2 p-4">
            {#if device_info == null}
                <div class="flex flex-row justify-center item-center w-full">
                    <LoadingSnake radius={1}/>
                </div>
            {:else}
                <div in:fade class="flex flex-col md:flex-row justify-between items-center w-full">
                    <div class="grid lg:grid-flow-col grid-rows-3">
                        {#each Object.entries(device_info) as [key, value]}
                            <p class="px-5"><strong>{key}</strong>: {value}</p>
                        {/each}
                    </div>
                    <div class="flex flex-row mt-6 md:mt-0 items-center">
                        <button on:click={Refresh} class="border-2 p-2 m-2 transition transition-duratin-300 hover:scale-110 rounded-xl border-white text-center">Refresh</button>
                    </div>
                </div>
            {/if}
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 p-2 mx-auto">
            <a href="/registers" on:click={() => $CurrentTable = coil_table ? {register_list: coil_table, type: ModbusTable.Coils} : null} class="flex flex-row justify-center items-center border-2 rounded-xl border-gray-600 text-gray-600 hover:text-white hover:border-white hover:scale-110 transition transition-duration-300 m-3 w-72" style="height: 37rem;"><Table register_list={coil_table} title="Coils"/></a>
            <a href="/registers" on:click={() => $CurrentTable = discrete_input_table ? {register_list: discrete_input_table, type: ModbusTable.DiscreteInputs} : null}  class="flex flex-row justify-center items-center border-2 rounded-xl border-gray-600 text-gray-600 hover:text-white hover:border-white hover:scale-110 transition transition-duration-300 m-3 w-72" style="height: 37rem;"><Table register_list={discrete_input_table} title="Discrete Inputs"/></a>
            <a href="/registers" on:click={() => $CurrentTable = holding_registers_table ? {register_list: holding_registers_table, type: ModbusTable.HoldingRegisters} : null}  class="flex flex-row justify-center items-center border-2 rounded-xl border-gray-600 text-gray-600 hover:text-white hover:border-white hover:scale-110 transition transition-duration-300 m-3 w-72" style="height: 37rem;"><Table register_list={holding_registers_table} title="Holding Registers"/></a>
            <a href="/registers" on:click={() => $CurrentTable = input_registers_table ? {register_list: input_registers_table, type: ModbusTable.InputRegisters} : null}  class="flex flex-row justify-center items-center border-2 rounded-xl border-gray-600 text-gray-600 hover:text-white hover:border-white hover:scale-110 transition transition-duration-300 m-3 w-72" style="height: 37rem;"><Table register_list={input_registers_table} title="Input Registers"/></a>
        </div>
    {/if}
</div>
