<script lang="ts"> 
    import { ModbusTable, function_code} from "$lib/modbus_table";
	import RegisterMap from "./registermap.svelte";
    export let ip: string;
    export let port: string;
    
    let address: number=0;
    let count: number=1;
    let selected_table = ModbusTable.HoldingRegisters;
    let func_code = function_code(selected_table);

    $: func_code = function_code(selected_table);
</script>
  
<div class=relative>
    <div class="fixed bg-black top-0 left-0 flex flex-row justify-between p-5 w-screen items-center z-10 bg-opacity-90">
        <a href="/" class="text-xl text-center text-gray-400 hover:text-white opacity-100">{ip}:{port}</a>
    
        <div class="flex flex-row">
            {#each Object.values(ModbusTable) as table, i}
                <input id={table + i} type="radio" bind:group={selected_table} value={table} class="sr-only">
                <label for={table + i} class:text-gray-500={selected_table != table} class="mx-2 hover:text-gray-200">{table}</label>
            {/each}
        </div>
    
        <div class="flex flex-col justify-center items-center">
            <form class="flex flex-col">
                <div class="relative flex flex-row h-fit">
                    <input type="text" class="text-sm w-20 bg-gray-800 p-2 mr-1 rounded-bl-xl focus:outline-none focus:ring-1 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={address} placeholder="0">
                    <input type="text" class="text-sm w-20 bg-gray-800 p-2 rounded-tr-xl focus:outline-none focus:ring-1 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={count} placeholder="1"> <!-- TODO -->
                    <div class="absolute -top-3 left-3 text-gray-400 text-m">address</div>
                    <div class="absolute -bottom-3 right-3 text-gray-400 text-m">count</div>
                </div>
            </form>
        </div>
    </div>
    
    <div class="mt-20">
        <RegisterMap {ip} {port} {address} {count} {func_code} />
    </div>
</div>