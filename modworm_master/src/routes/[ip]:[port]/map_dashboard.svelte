<script lang="ts"> 
    import { ModbusTable, function_code} from "$lib/modbus_table";
    import { ModbusDataType, data_type } from "$lib/modbus_data_type";
	import RegisterMap from "./register_map.svelte";
    export let ip: string;
    export let port: string;
    
    let address: number = 0;
    let count: number = 1;

    let addr: number = 0;
    let cnt: number = 1;

    let selected_table = ModbusTable.HoldingRegisters;
    let selected_data_type = ModbusDataType.Hex;
    let func_code = function_code(selected_table);
    let type = data_type(selected_data_type);

    $: func_code = function_code(selected_table);
    $: type = data_type(selected_data_type);
    
    function update_map() {
        address = addr;
        count = cnt;
    }

</script>
  
<div class="relative">
    <div class="fixed bg-black top-0 left-0 flex flex-row justify-between p-5 w-screen items-center z-10 bg-opacity-90">
        <a href="/" class="text-xl ml-5 text-center text-gray-400 hover:text-white opacity-100">{ip}:{port}</a>
    
        <div class="flex flex-row lg:flex-col">
            <div class="flex lg:flex-row flex-col">
                {#each Object.values(ModbusTable) as table, i}
                    <input id={table + i} type="radio" bind:group={selected_table} value={table} class="sr-only">
                    <label for={table + i} class:text-gray-500={selected_table != table} class="mx-2 text-nowrap text-center hover:text-gray-200">{table}</label>
                {/each}
            </div>
            <div class="flex lg:flex-row flex-col justify-center">
                {#each Object.values(ModbusDataType) as data_type, i}
                    <input id={data_type + i} type="radio" bind:group={selected_data_type} value={data_type} class="sr-only">
                    <label for={data_type + i} class:text-gray-500={selected_data_type != data_type} class="mx-2 text-nowrap text-center hover:text-gray-200">{data_type}</label>
                {/each}
            </div>
        </div>
        <div class="flex flex-col justify-center items-center">
            <form class="flex lg:flex-row flex-col" on:submit={update_map}>
                <div class="relative flex flex-row h-fit">
                    <input type="text" class="text-sm w-20 bg-gray-800 p-2 mr-1 rounded-bl-xl focus:outline-none focus:ring-1 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={addr} placeholder="0">
                    <input type="text" class="text-sm w-20 bg-gray-800 p-2 rounded-tr-xl focus:outline-none focus:ring-1 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={cnt} placeholder="1"> <!-- TODO -->
                    <div class="absolute -top-3 left-3 text-gray-400 text-m">address</div>
                    <div class="absolute -bottom-3 right-3 text-gray-400 text-m">count</div>
                </div>
                <button class="text-3xl text-gray-500 lg:px-5 hover:text-white">&rarr;</button>
            </form>
        </div>
    </div>
    
    <div class="lg:mt-24 mt-36 mx-10">
        <RegisterMap {ip} {port} {address} {count} {func_code} {type} />
    </div>
</div>