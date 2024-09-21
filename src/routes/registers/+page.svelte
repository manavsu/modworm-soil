<script lang="ts">
    import Title from '$lib/title.svelte';
    import { ConnectedSocket, Working, CurrentTable, SelectedDataType} from '$lib/store';
    import { fade } from 'svelte/transition';
    import { BASE_URL } from '$lib/env'; 
    import LoadingSnake from '$lib/loading_snake.svelte';
    import Register from './register.svelte';
    import { onMount } from 'svelte';
    import { ModbusDataType, data_type_to_int, int_to_data_type } from "$lib/modbus_data_type";
    import { ReadRegisters } from "$lib/modbus_client";
    import type { RegisterStore } from "$lib/register_store";
    import { ModbusTable, function_code} from "$lib/modbus_table";
    import { SelectedRegisters, NamedRegisters } from "$lib/store";
    
    let error: string | null = null;

    interface RegisterGroup {
        address: number;
        count: number;
        registers: Array<RegisterStore>;
    }
	let read_error: any;
	let register_groups: Array<RegisterGroup> = [];

	async function ReadAllRegisters() {
        read_error = null;
        if ($CurrentTable == null || $ConnectedSocket == null){
            register_groups = [];
            return;
        }
		try {
            for (let i = 0; i < $CurrentTable.register_list.length; i++) {
			    const result = await ReadRegisters($ConnectedSocket.address, $ConnectedSocket.port, function_code($CurrentTable.type), $CurrentTable.register_list[i][0], $CurrentTable.register_list[i][1], data_type_to_int($SelectedDataType));
                let registers: Array<RegisterStore> = [];
                for (let j = 0; j < $CurrentTable.register_list[i][1]; j++) {
                    registers[j] = { address: $CurrentTable.register_list[i][0] + j, value: result[j], type: $SelectedDataType};
                }
                register_groups[i] = {address: $CurrentTable.register_list[i][0], count: $CurrentTable.register_list[i][1], registers: registers};
            }
			
			register_groups = [...register_groups];
		} catch (error) {
			read_error = error;
		}
	}

    function name_registers() {
        console.log($SelectedRegisters);
        console.log($NamedRegisters);
        for (let i = 0; i < $SelectedRegisters.length; i++) {
            if ($NamedRegisters.findIndex(reg => reg.address === $SelectedRegisters[i].address) === -1){                
                $NamedRegisters.push($SelectedRegisters[i]);
            }
        }
        $SelectedRegisters = [];
        register_groups = [...register_groups];
    }

	let intervalId: number;
	onMount(() => {
		intervalId = setInterval(async () => {
			await ReadAllRegisters();
		}, 1000);
		return () => {
			clearInterval(intervalId);
		};
	});
</script>
<!-- disabled={$SelectedRegisters.length == 0}  -->
<style lang="postcss">
	.grid-col-fill {
		grid-template-columns: repeat(auto-fill, minmax(144px, 1fr));
	}
</style>

<div class="flex flex-row h-full">
    <div class="flex flex-col items-center min-w-32 gap-2 pt-9">
        <div class="border w-2/3 border-gray-500"/>
        <div>Data Type</div>
        <div class="flex flex-col justify-center gap-1">
            {#each Object.values(ModbusDataType) as data_type, i}
                <input id={data_type + i} type="radio" bind:group={$SelectedDataType} value={data_type} class="sr-only">
                <label for={data_type + i} class:text-gray-500={$SelectedDataType != data_type} class="mx-2 text-nowrap text-center hover:text-gray-200">{data_type}</label>
            {/each}
        </div>
        <div class="border w-2/3 border-gray-500"/>
        <button on:click={name_registers} class="text-gray-500 hover:text-white">Name</button>
        <div class="border w-2/3 border-gray-500"/>
    </div>
    <div class="h-full border border-gray-600"/>
    <div in:fade={{delay: 200, duration:200}} class="flex flex-col h-full w-full">
        <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2 p-2">
            {#if !error}
                <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                    <Title>Registers</Title>
                </div>
            {:else}
                <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                    <h2 class="text-center text-xl text-rose-900">{error}</h2>
                </div>
            {/if}
        </div>
        {#if !$CurrentTable}
            <div class="flex flex-col justify-center items-center flex-grow text-2xl">
                <p class="text-center">No selected table, select one from the tables page.</p>
                <a href="/tables" class="border-2 px-10 py-2 mt-8 clickable border-white text-center">Tables</a>
            </div>
        {:else}
            <div class="relative flex flex-col overflow-auto h-full">
                <div class="flex flex-col mx-2 p-2 overflow-auto scrollbar-thin h-full">
                    {#each register_groups as group}
                        <div class="grid grid-col-fill gap-1 justify-items-center">
                            {#each group.registers as register}
                                <Register register={register}/>
                            {/each}
                        </div>
                    {/each}
                    <!-- <div class="absolute left-2 top-0 z-10">
                        <div class="border-2 border-gray-500 flex items-center justify-center rounded-xl">
                            <div class="bg-black rounded-lg p-4 shadow-lg">
                                <h2 class="text-xl font-bold mb-4">Popup Content</h2>
                                <p>This is the content of the popup.</p>
                                <button class="bg-blue-500 text-white px-4 py-2 rounded-lg mt-4">Close</button>
                            </div>
                        </div>
                    </div> -->
                </div>
            </div>
        {/if}
    </div>
</div>