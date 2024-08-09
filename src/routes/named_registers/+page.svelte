<script>
    import Title from '$lib/title.svelte';
    import { fade } from 'svelte/transition';
</script>
<div in:fade={{delay: 200, duration:200}} class="flex flex-col h-full w-full overflow-auto scrollbar-thin">
    <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
        <Title>Named Registers</Title>
    </div>
</div>
